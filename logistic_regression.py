# Imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# load dataset
alltopcountries = pd.read_csv("VossMaria_CPE_590_Project/Datasets/top26_numlabels.csv")

# Create the Logistic Regression model
x = alltopcountries[['Material Number Labels', 'Geo Number Labels', 'OBS_VALUE']].to_numpy() # features
y = alltopcountries[['Partner Number Labels']].to_numpy().ravel() # output
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=16)

# instantiate the model (using the default parameters)
logreg = LogisticRegression(random_state=16, max_iter=1000)

# fit the model with data
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)