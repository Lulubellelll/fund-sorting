import pandas as pd 

def compare_index(funds_old, funds_new):

    funds_new.insert(0, "change", {})

    for index, fund in funds_new.iterrows():

        fund_code = fund.KOD 

        current_index = index + 1
        old_index = funds_old.loc[funds_old["KOD"] == fund_code].index[0] + 1 

        diff = old_index - current_index
        funds_new.at[index, "change"] = diff
    

    return funds_new.astype({"change": int})