# Logistic Regression for Turkiye
# First, need to get a dataset for only Turkey's imports (EU exports)
import pandas as pd

'''
Step 1: Filtering
'''

# load dataset
allcountries = pd.read_csv("VossMaria_CPE_590_Project/aggregate_trash.csv")

# extract only the TOTAL's and save them as a new smaller csv
exports = allcountries.loc[allcountries['stk_flow'] == "EXP"]

# We are only looking into tonnes of trash, not the amount of thousands of euros the trash was valued at
exp_tonnes = exports.loc[exports['unit'] == "T"]

# Singling out Turkey (aka Turkiye)
turkiye_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "TR"]
turkiye_exp_tonnes.to_csv('turkiye_exp_tonnes.csv')

