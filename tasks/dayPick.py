from datetime import date, timedelta


def get_workdoy_yesterday():

    if date.today().strftime("%a") == "Mon":        
        delta = 3
    else:
        delta = 1

    yesterday = (date.today() - timedelta(days = delta)) 
    
    return yesterday

