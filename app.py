from flask import Flask, render_template,request
import pickle
import numpy as np
import sklearn


app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/", methods = ["GET"])
def my_form():
    return render_template("index.html")

@app.route("/",  methods = ["POST"])
def data():
    if request.method == "POST":
        GUI_KM = request.form.get("km")
        GUI_ONWER = request.form.get("owner")
        GUI_MILEAGE = request.form.get("mileage")
        GUI_CC = request.form.get("cc")
        GUI_BHP = request.form.get("bhp")
        GUI_SEATS = request.form.get("seats")
        GUI_AGE = request.form.get("age")
        GUI_FUEL = request.form.get("fuel")
        GUI_TRANSMISSION = request.form.get("transmission")

        user_km_driver = int(GUI_KM)
        user_owner = float(GUI_ONWER)
        user_mileage = float(GUI_MILEAGE)
        user_engine = float(GUI_CC)
        user_power = float(GUI_BHP)
        user_seats = float(GUI_SEATS)
        user_age = int(GUI_AGE)
        user_fuel = GUI_FUEL
        user_transmission = GUI_TRANSMISSION

        if user_fuel == "CNG":
            if user_transmission == "Automatic":
                preditcion = [user_km_driver,user_owner,user_mileage,user_engine,user_power,user_seats,user_age,1,0,0,0,1,0]
            if user_transmission == "Manual":
                preditcion = [user_km_driver,user_owner,user_mileage,user_engine,user_power,user_seats,user_age,1,0,0,0,0,1]
        if user_fuel == "Diesel":
            if user_transmission == "Automatic":
                preditcion = [user_km_driver,user_owner,user_mileage,user_engine,user_power,user_seats,user_age,0,1,0,0,1,0]
            if user_transmission == "Manual":
                preditcion = [user_km_driver,user_owner,user_mileage,user_engine,user_power,user_seats,user_age,0,1,0,0,0,1]
        if user_fuel == "LPG":
            if user_transmission == "Automatic":
                preditcion = [user_km_driver,user_owner,user_mileage,user_engine,user_power,user_seats,user_age,0,0,1,0,1,0]
            if user_transmission == "Manual":
                preditcion = [user_km_driver,user_owner,user_mileage,user_engine,user_power,user_seats,user_age,0,0,1,0,0,1]
        if user_fuel == "Petrol":
            if user_transmission == "Automatic":
                preditcion = [user_km_driver,user_owner,user_mileage,user_engine,user_power,user_seats,user_age,0,0,0,1,1,0]
            if user_transmission == "Manual":
                preditcion = [user_km_driver,user_owner,user_mileage,user_engine,user_power,user_seats,user_age,0,0,0,1,0,1]
                
        prediction_price = int(model.predict([preditcion]))

    return render_template('index.html',prediction_price="You Can Sell The Car at {} Rs".format(prediction_price))

if __name__ == "__main__":
        app.run()
