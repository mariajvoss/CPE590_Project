import numpy as np
import pandas as pd

'''
Find Top Importers of Waste 

    Find all the total wastes
    Add up all the total wastes 
        There are multiple total wastes per year per country
    store in a python dictionary
    Sort the dictionary and only keep the top 25 importers for our dataset

'''


'''
Step 1: Filtering
'''
'''
# load dataset
allcountries = pd.read_csv("aggregate_trash.csv")

# extract only the TOTAL's and save them as a new smaller csv
totals = allcountries.loc[allcountries['rawmat'] == "TOTAL"]


# only keep the exports = stuff leaving the EU
total_exports = totals.loc[totals['stk_flow'] == "EXP"]

# We are only looking into tonnes of trash, not the amount of thousands of euros the trash was valued at
total_exp_tonnes = total_exports.loc[total_exports['unit'] == "T"]


# Create a list of totals for each country
total_total_exp_tonnes = total_exp_tonnes.loc[total_exp_tonnes['geo'] == "EU27_2020"]
total_total_exp_tonnes.to_csv('total_total_exp_tonnes.csv')
'''


# Group the totals of each non-EU country collecting trash together
total_total_exp_tonnes = pd.read_csv('total_total_exp_tonnes.csv')

# Delete columns that we don't need --> we only need 'partner' and 'OBS_VALUE'
needed_columns = total_total_exp_tonnes.drop(columns=['Unnamed: 0', 'stk_flow', 'rawmat', 'unit', 'geo', 'TIME_PERIOD'])

# Create a dictionary to iterate through the rows. If a country is included in the dictionary already as a key, the OBS_VALUE will be added to the key's value. 
needed_columns = needed_columns.reset_index()  # make sure indexes pair with number of rows
dictionary = {}
for index, row in needed_columns.iterrows():
    key = row['partner']
    value = row['OBS_VALUE']
    if key in dictionary:
        dictionary[key] = dictionary[key] + value

    else:
        dictionary[key] = value

print(len(dictionary))
# There are 215 keys, which was expected. 

# Sort the dictionary starting with the highest values: 
sorting = dict(reversed(sorted(dictionary.items(), key=lambda item: item[1])))
print(sorting)


# Get the total trash exported for each country, added up for all the years
#sums = needed_columns.groupby('partner')['OBS_VALUE'].transform('sum')
#print(sums)

# Encoding the numbers to their corresponding countries



# Add up the totals for each country