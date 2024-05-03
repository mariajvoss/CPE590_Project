# Logistic Regression for Turkiye
# First, need to get a dataset for only Turkey's imports (EU exports)
import pandas as pd



# load dataset
allcountries = pd.read_csv("VossMaria_CPE_590_Project/Datasets/aggregate_trash.csv")

# extract only the TOTAL's and save them as a new smaller csv
exports = allcountries.loc[allcountries['stk_flow'] == "EXP"]

# We are only looking into tonnes of trash, not the amount of thousands of euros the trash was valued at
exp_tonnes = exports.loc[exports['unit'] == "T"]

# Delete columns that we don't need 
#exp_tonnes = exp_tonnes_unnamedc.drop(columns=['Unnamed: 0'])

'''
Turkey
'''
# Singling out Turkey (aka Turkiye)
turkiye_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "TR"]
turkiye_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/turkiye_exp_tonnes.csv')


'''
China including Hong Kong
'''
# Singling out China including Hong Kong
china_HK_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "CN"]
china_HK_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/China_HK_exp_tonnes.csv')

'''
India
'''
# Singling out India
India_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "IN"]
India_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/India_exp_tonnes.csv')


'''
United Kingdom
'''
# Singling out United Kingdom
uk_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "UK"]
uk_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/UK_exp_tonnes.csv')

'''
Switzerland
'''
# Singling out Switzerland
Switzerland_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "CH"]
Switzerland_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Switzerland_exp_tonnes.csv')

'''
Norway
'''
# Singling out Norway
Norway_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "NO"]
Norway_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Norway_exp_tonnes.csv')

'''
Indonesia
'''
# Singling out Indonesia
Indonesia_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "ID"]
Indonesia_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Indonesia_exp_tonnes.csv')

'''
Egypt
'''
# Singling out Egypt
Egypt_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "EG"]
Egypt_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Egypt_exp_tonnes.csv')

'''
United States
'''
# Singling out United States
unitedStates_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "US"]
unitedStates_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/US_exp_tonnes.csv')

'''
Hong Kong
'''
# Singling out Hong Kong
hongKong_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "HK"]
hongKong_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/HongKong_exp_tonnes.csv')

'''
Pakistan
'''
# Singling out Pakistan
Pakistan_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "PK"]
Pakistan_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Pakistan_exp_tonnes.csv')

'''
Greece
'''
# Singling out Greece
Greece_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "EL"]
Greece_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Greece_exp_tonnes.csv')

'''
South Korea
'''
# Singling out South Korea
southKorea_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "KR"]
southKorea_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/SouthKorea_exp_tonnes.csv')

'''
Vietnam
'''
# Singling out Vietnam
Vietnam_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "VN"]
Vietnam_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Vietnam_exp_tonnes.csv')

'''
Morocco
'''
# Singling out Morocco
Morocco_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "MA"]
Morocco_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Morocco_exp_tonnes.csv')

'''
Taiwan
'''
# Singling out Taiwan
Taiwan_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "TW"]
Taiwan_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Taiwan_exp_tonnes.csv')

'''
Malaysia
'''
# Singling out Malaysia
Malaysia_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "MY"]
Malaysia_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Malaysia_exp_tonnes.csv')

'''
Thailand
'''
# Singling out Thailand
Thailand_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "TH"]
Thailand_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Thailand_exp_tonnes.csv')

'''
Ukraine
'''
# Singling out Ukraine
Ukraine_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "UA"]
Ukraine_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Ukraine_exp_tonnes.csv')

'''
North Macedonia
'''
# Singling out North Macedonia
northMacedonia_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "MK"]
northMacedonia_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/NorthMacedonia_exp_tonnes.csv')

'''
Tunisia
'''
# Singling out Tunisia
Tunisia_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "TN"]
Tunisia_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Tunisia_exp_tonnes.csv')

'''
Serbia
'''
# Singling out Serbia
Serbia_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "RS"]
Serbia_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Serbia_exp_tonnes.csv')

'''
United Arab Emirates
'''
# Singling out United Arab Emirates
arabEmirates_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "AE"]
arabEmirates_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/UnitedArabEmirates_exp_tonnes.csv')

'''
Bangladesh
'''
# Singling out Bangladesh
Bangladesh_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "BD"]
Bangladesh_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Bangladesh_exp_tonnes.csv')

'''
Russia
'''
# Singling out Russia
Russia_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "RU"]
Russia_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Russia_exp_tonnes.csv')

'''
Moldova
'''
# Singling out Moldovia
moldova_exp_tonnes = exp_tonnes.loc[exp_tonnes['partner'] == "MD"]
moldova_exp_tonnes.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/Moldova_exp_tonnes.csv')


# Combine all the dataframes into one big dataset
alldataframes = [turkiye_exp_tonnes, china_HK_exp_tonnes, India_exp_tonnes, uk_exp_tonnes, Switzerland_exp_tonnes, Norway_exp_tonnes, Indonesia_exp_tonnes, Egypt_exp_tonnes, unitedStates_exp_tonnes, hongKong_exp_tonnes, Pakistan_exp_tonnes, Greece_exp_tonnes, southKorea_exp_tonnes, Vietnam_exp_tonnes, Morocco_exp_tonnes, Taiwan_exp_tonnes, Malaysia_exp_tonnes, Thailand_exp_tonnes, Ukraine_exp_tonnes, northMacedonia_exp_tonnes, Tunisia_exp_tonnes, Serbia_exp_tonnes, arabEmirates_exp_tonnes, Bangladesh_exp_tonnes, Russia_exp_tonnes, moldova_exp_tonnes]
merged_list = pd.concat(alldataframes)
merged_list.to_csv('VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/All_Top_Countries.csv')


