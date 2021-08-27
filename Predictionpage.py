import pickle

model = pickle.load(open("model.pkl","rb"))

user_km_driver = int(input("Enter How Many Km Driven Car You Want :- "))
user_owner = float(input("How Many Owner :- "))
user_mileage = float(input("Mileage in kmpl :- "))
user_engine = float(input("How Many CC Car You Want :-"))
user_power = float(input("Enter BHP :- "))
user_seats = float(input("How Many Seats You Want :- "))
user_age = int(input("How old :- "))
user_fuel = input("1.CNG \n2.Diesel \n3.LPG \n4.Petrol \nEnter Here :- ")
user_transmission = input("1.Automatic \n2.Manual \nEnter Here :- ")

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


print(model.predict(preditcion))