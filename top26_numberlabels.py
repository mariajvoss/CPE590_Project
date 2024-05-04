'''
This Python script exists to perform Logistic regression on the aggregate_trash dataset. 
The features are exporting country (geo), type of trash, and amount of trash. 
The classes are which country the trash will go to (partner). 

Types of trash are in Datasets/material_labels.csv  
Total
Paper and cardboard
Plastics including rubber
Plastics
Rubber
Wood
Textiles
Textiles - synthetic
Textiles - natural
Glass
Organic
Organic - animal origin
Organic - vegetal origin
Mineral
Metal
Metal - ferrous
Metal - non ferrous
Metal - non ferrous - precious metals
Metal - non ferrous - copper aluminium and nickel
Metal - non ferrous - other
Not specified

'''

# Imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


'''
Preprocessing
'''
# We want to keep the exports and the quantities in metric tonnes
# load dataset
alltopcountries = pd.read_csv("VossMaria_CPE_590_Project/Datasets/Top26_Partner_Countries/All_Top_Countries.csv")

# Delete columns that we don't need --> we don't need the first column of numbers, the year, or the column denoting metric tonnes
aggregate_trash = alltopcountries.drop(columns=['Unnamed: 0', 'unit', 'TIME_PERIOD'])
# Main dataset preprocessing done for now

# Import the partner_labels and geo_labels datasets
partner_labels = pd.read_csv("VossMaria_CPE_590_Project/Datasets/partner_labels.csv")
partner_labels.rename(columns={"Labels": "Partner_Labels", "Codes": "Partner_Codes"}, inplace = True) #Rename the columns
geo_labels = pd.read_csv("VossMaria_CPE_590_Project/Datasets/geo_labels.csv")
geo_labels.rename(columns={"Labels": "Geo_Labels", "Codes": "Geo_Codes"}, inplace = True) #Rename the columns
material_labels = pd.read_csv("VossMaria_CPE_590_Project/Datasets/material_labels.csv")
material_labels.rename(columns={"Labels": "Material_Labels", "Codes": "Material_Codes"}, inplace = True) #Rename the columns

# Assign numbers to the partner and geo labels and types of trash (rawmat)
# Create a list of numbers to replace the labels with
# None of the numbers will be repeated since they are labels
partner_numbers = list(range(0, len(partner_labels)))
geo_numbers = list(range(len(partner_labels), len(partner_labels) + len(geo_labels)))
material_numbers = list(range(geo_numbers[-1] + 1, geo_numbers[-1] + 1 + len(material_labels)))

# Adding the lists of numbers to their respective dataframes
partner_labels.insert(1, "Partner Number Labels", partner_numbers, True)
partner_labels.to_csv('VossMaria_CPE_590_Project/Datasets/num_partnerlabels.csv')
geo_labels.insert(1, "Geo Number Labels", geo_numbers, True)
geo_labels.to_csv('VossMaria_CPE_590_Project/Datasets/num_geolabels.csv')
material_labels.insert(1, "Material Number Labels", material_numbers, True)
material_labels.to_csv('VossMaria_CPE_590_Project/Datasets/num_materiallabels.csv')

# Map the partner, geo, and material numbers to their names in the alltopcountries dataset
aggregate_trash = pd.merge(aggregate_trash, partner_labels, left_on='partner', right_on='Partner_Codes')
aggregate_trash = pd.merge(aggregate_trash, geo_labels, left_on='geo', right_on='Geo_Codes')
aggregate_trash = pd.merge(aggregate_trash, material_labels, left_on='rawmat', right_on='Material_Codes')
aggregate_trash = aggregate_trash.drop(columns=['Geo_Codes', 'Material_Codes', 'Partner_Codes'])

print(aggregate_trash.columns.tolist())
# Reorder the columns to make reading the dataframe easier
top26_numlabels = aggregate_trash[['stk_flow', 'rawmat', 'Material_Labels', 'Material Number Labels', 'partner', 'Partner_Labels', 'Partner Number Labels', 'geo', 'Geo_Labels', 'Geo Number Labels', 'OBS_VALUE']]
print(type(top26_numlabels))

top26_numlabels.to_csv('VossMaria_CPE_590_Project/Datasets/top26_numlabels.csv')

