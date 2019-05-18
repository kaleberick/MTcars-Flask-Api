#!/usr/bin/env python3
import pandas
from sklearn.linear_model import LinearRegression


# Load mtcars data
cars = pandas.read_csv('scripts/mtcars.csv')

# Drop irrelevant columns for training
keep = ['cyl','disp','hp','drat','wt','qsec']

# Split up dependent and response variables
depend = cars[keep]
response = cars['mpg']

# Fit a linear model
predicted_mpg = LinearRegression().fit(depend, response)


def predict(json_input):
	df = pandas.DataFrame(json_input, index=[0])
	x = df[keep]
	result = predicted_mpg.predict(x)
	return result[0]

