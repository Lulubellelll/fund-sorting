import os 
import locale
import gspread
import logging
import requests
import pandas as pd 
import logging.handlers
from bs4 import BeautifulSoup
from datetime import date, timedelta
from tasks.sort import write_and_sort
from tasks.compare import compare_index
from tasks.credentials import credentials


# Setting locale time for datetime
locale.setlocale(locale.LC_TIME, "tr_TR")

# Setting logger 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8"
)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


# Scraping the data from web
r = requests.get("https://www.yatirimnedir.com/fon-filtreleme")
soup = BeautifulSoup(r.content, "lxml")

# Getting the table 
table = soup.find("div", attrs={"role": "table"})
rows = table.find_all("div", attrs={"role": "row"})[1:]


# Defining headers from table and creating 
# empty DataFrame with them
headers = [
            _.text
            if _.text[-1] != "▲"
            else
            _.text[:-1] 
            for _ in table.find_all("div", attrs={"role": "columnheader"})
]

funds = pd.DataFrame(columns=headers)


# Writing data into DataFrame and sorting it
funds_new = write_and_sort(rows=rows, funds=funds, headers=headers)

logger.info("Fund Data was Scraped")

# Authenticating the service account
gc = gspread.service_account_from_dict(credentials)
sh = gc.open("Aylık Fon Getiri")

# Definign today and yesterday
today = date.today().strftime("%d %B %Y")
yesterday = (date.today() - timedelta(days = 1)).strftime("%d %B %Y")

# Defining worksheets
ws_yest = sh.worksheet(yesterday)
ws_tod = ws_yest.duplicate(new_sheet_name=today, insert_sheet_index=0)

# Getting old fund data
old_data = ws_yest.get_all_values()
funds_old = pd.DataFrame(old_data[1:], columns=old_data[0])

logger.info("Olf Funds Data was Scraped")

# Add change column to the new funds and
# compare with the old funds
funds_new = compare_index(funds_old, funds_new)


# Saving new funds to the today's workshet
funds = funds_new.values.tolist()
headers = funds_new.astype('object').columns.tolist()

ws_tod.update(range_name="A2", values=funds)
ws_tod.update(range_name="A1", values=[headers])

logger.info("Olf Funds Data was Pushed into Sheets")
