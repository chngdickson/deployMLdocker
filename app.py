from flask import Flask,render_template, request # , url_for
import pandas as pd
# import pickle
from sklearn.linear_model import LinearRegression
# import joblib

import os
os.chdir(r"D:\360DigiTMG\Trainings\MLOps\Presentations\03_Docker_ML\ML_model")

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	df= pd.read_csv("Salary_Data.csv")
	
	regressor = LinearRegression()
	regressor.fit(df.YearsExperience.values.reshape(30,1),df.Salary)

	if request.method == 'POST':
		value = request.form['val']
		pred = pd.DataFrame([value])
		pred.columns=['YearsExperience']
		my_pred = regressor.predict(pred)
	return render_template('result.html',prediction=my_pred)



if __name__ == '__main__':
	app.run(debug=True,use_reloader=False)