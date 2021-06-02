# the csv file has around 8200 rows, data taken at every 3 seconds 
	#from 12:00 am to 7:00 pm

# 7 hours = 25000 seconds
	#i want to predict temperature at 10:00 am
		#then i am going to add 10800 seconds(3 hours) 
			# total 25000 + 10800 = 35800 seconds

#----------------------------------------------------------------------------------------------------------------------

import pandas as pd  
from sklearn.linear_model import LinearRegression

df = pd.read_csv("out.csv")

X = df['Time in seconds'].values.reshape(-1,1)
y = df['Temperature'].values.reshape(-1,1)

regressor = LinearRegression() 
regressor.fit(X, y)

y_pred = regressor.predict([[35000]])

print("Prediction : {}".format(y_pred[0][0]))

