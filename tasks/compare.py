import pandas as pd 


def compare_index(funds_old, funds_new):

    # Insert column named "PLACE"
    funds_new.insert(0, "PLACE", {})

    # Getting new index
    for index, fund in funds_new.iterrows():

        fund_code = fund.KOD 

        current_index = index + 1

        old_row = funds_old.loc[funds_old["KOD"] == fund_code]
        old_index = index + 1 if len(old_row) == 0 else funds_old.loc[funds_old["KOD"] == fund_code].index[0] + 1

        # Write the new index diff on "PLACE" column
        diff = old_index - current_index
        funds_new.at[index, "PLACE"] = diff
    
    # Returning new list 
    return funds_new.astype({"PLACE": int})