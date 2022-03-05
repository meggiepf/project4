import pandas as pd
import numpy as np
import sqlalchemy
import csv
import time
import pickle
from config import password
from decimal import Decimal
from flask import Flask, render_template, redirect
from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask import Response
from flask import request
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, session
from sqlalchemy import create_engine, func
from sqlalchemy_utils import database_exists, create_database
from flask import Flask, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{password}@localhost:5432/project4'
sql = SQLAlchemy(app)

# Creating Engine
engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/project4")
if not database_exists(engine.url):
    create_database(engine.url)

# reflecting database
Base = automap_base()

# reflecting tables
Base.prepare(engine, reflect=True)

# Load ML model
model = pickle.load(open('model.pkl', 'rb')) 

# Load initial data to sql
data = pd.read_csv("clean_loan.csv")
data["GRADE"].replace({"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6 },inplace=True)
try:
    data.to_sql(name='initial_loan_data', con=engine, if_exists='fail', index=False)
except ValueError:
    pass

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('index.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('index.html', 
                               result = 'The patient is likely to have heart disease!')

#Run the application
if __name__ == "__main__":
    app.run(debug=True)