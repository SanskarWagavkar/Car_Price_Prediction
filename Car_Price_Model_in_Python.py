import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
import pickle

## Owner to int function
def Owner_to_int(Value):
    if Value == "First Owner":
        return int(1)
    if Value == "Second Owner":
        return int(2)
    if Value == "Third Owner":
        return int(3)
    if Value == "Fourth & Above Owner":
        return int(4)
    if Value == "Test Drive Car":
        return None

    
##  Mileage to int function   
def Mileage_to_int(Value_1):
    a = str(Value_1)
    b = a.split(" ")
    return float(b[0])    


## engine to int data type
def engine_to_int(Value_2):
    a = str(Value_2)
    b = a.split(" ")
    return float(b[0])


## power to float data type
def power_to_int(Value_3):
    a = str(Value_3)
    b = a.split(" ")
    return float(b[0])


## creating Age column
def Age_col(Value_4):
    a = 2021-Value_4
    return a


def main_model(preditcion):
    ## importing data-set
    df = pd.read_csv("Car details v3.csv")

    ## cleaning NA values
    df_clean = df.dropna()

    ## cleaning dulicate values
    df_clean.drop_duplicates()

    ## drop useless columns
    df_clean.drop(["name","seller_type","torque"],axis=1, inplace=True)

    ## converting owner to int data-type
    df_preprocessing = df_clean.copy()
    df_preprocessing["owner"] = df_preprocessing.owner.apply(Owner_to_int)
    df_preprocessing_Owner =  df_preprocessing.dropna()

    ## converting mileage to int data type
    df_preprocessing_Owner["mileage"] = df_preprocessing_Owner.mileage.apply(Mileage_to_int)

    ## Copying in new data-frame
    df_preprocessing_Mileage = df_preprocessing_Owner.copy()
    df_preprocessing_engine = df_preprocessing_Mileage.copy()

    ## converting engine to int 
    df_preprocessing_engine["engine"] = df_preprocessing_engine.engine.apply(engine_to_int)

    ## converting power to float
    df_preprocessing_Power = df_preprocessing_engine.copy()
    df_preprocessing_Power["max_power"] = df_preprocessing_Power.max_power.apply(power_to_int)

    ## Creating Age column
    df_preprocessing_Age = df_preprocessing_Power.copy()
    df_preprocessing_Age["Age"] = df_preprocessing_Age.year.apply(Age_col)

    ## Droping year column
    df_preprocessing_Age.drop(["year"], axis=1, inplace=True)

    ## checking outlier in age column and seats column
    df_preprocessing_Outlier = df_preprocessing_Age.copy() 
    df_preprocessing_Outlier_age =  df_preprocessing_Outlier[(df_preprocessing_Outlier.Age < 20)]
    df_preprocessing_Outlier_seats =  df_preprocessing_Outlier_age[(df_preprocessing_Outlier_age.seats < 9)]

    ## one hot encoding 
    df_preprocessing_Outlier_Encoding = pd.get_dummies(df_preprocessing_Outlier_seats)

    ## spliting into test and train
    X = df_preprocessing_Outlier_Encoding.drop(["selling_price"], axis=1)
    y = df_preprocessing_Outlier_Encoding.selling_price

    ## dividing into xtrain, xtest, ytrain, ytest
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state= 50)

    ## fitting my data into model of decision tree regression
    dtr = DecisionTreeRegressor()
    dtr.fit(X_train,y_train)

    ## applying K-Fold cross vaildation on train data set  
    cvs = cross_val_score(dtr, X_train, y_train, cv=10)
    print(f"My Average score is :- {cvs.mean()} on training Data")

    ## applying K-Flod cross validation on test data-set
    cvs_1 = cross_val_score(dtr, X_test, y_test, cv=10)
    print(f"My Average score is :- {cvs_1.mean()} on tesing Data")

    ## predicting using predict function        
    Predict_Price = dtr.predict([preditcion])
    print(f"The Price of an car is :- {int(Predict_Price)} Rs")
    pickle.dump(dtr, open("model.pkl","wb"))
    

## doing prediction 
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

## Calling model        
main_model(preditcion)  
    


