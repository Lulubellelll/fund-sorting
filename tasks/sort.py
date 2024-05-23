import pandas as pd

def write_and_sort(rows, funds, headers):

    # Write the data into DataFrame
    for row in rows:

        cells = row.find_all("div", attrs={"role": "cell"})
        fund = pd.DataFrame([[cell.text for cell in cells]], columns=headers)


        funds = pd.concat([funds, fund])

    # Changing the data types of the columns 
    convert_dict = {
                    "GÜNLÜK": float,
                    "HAFTALIK": float,
                    "1 AY": float,
                    "3 AY": float,
                    "6 AY": float,
                    "1 YIL": float,
                    "YBB": float,
                    "3 YIL": float,
                    "5 YIL": float
    }

    funds = funds.astype(convert_dict)

    # Sorting funds for 1 month interval
    sorted_funds = funds.sort_values(by=["1 AY"], ascending=False, ignore_index=True)

    return sorted_funds