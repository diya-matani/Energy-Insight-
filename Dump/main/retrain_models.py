import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

def retrain():
    print("Retraining models with optimized parameters (n_estimators=10, n_jobs=-1)...")
    
    # 1. Heating and Cooling Load
    print("Loading ENB2012_data.csv...")
    if not os.path.exists("ENB2012_data.csv"):
        print("Error: ENB2012_data.csv not found!")
        return

    df = pd.read_csv("ENB2012_data.csv")
    X = df.drop(columns=['Y1', 'Y2'])
    y_heat = df['Y1']
    y_cool = df['Y2']

    # Heating Model
    print("Training Heat Load Model...")
    X_train_h, X_test_h, y_train_h, y_test_h = train_test_split(X, y_heat, test_size=0.2, random_state=42)
    # Optimized: n_estimators=10, n_jobs=-1
    clf_heat = RandomForestRegressor(n_estimators=10, n_jobs=-1, random_state=42)
    clf_heat.fit(X_train_h, y_train_h)
    joblib.dump(clf_heat, 'heatLoad.joblib')
    print("Saved heatLoad.joblib")

    # Cooling Model
    print("Training Cool Load Model...")
    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y_cool, test_size=0.2, random_state=42)
    clf_cool = RandomForestRegressor(n_estimators=10, n_jobs=-1, random_state=42)
    clf_cool.fit(X_train_c, y_train_c)
    joblib.dump(clf_cool, 'coolLoad.joblib')
    print("Saved coolLoad.joblib")

    # 2. Appliances
    print("Loading training.csv...")
    if not os.path.exists("training.csv"):
        print("Error: training.csv not found!")
        return

    df_appliances = pd.read_csv("training.csv")
    drop_cols = ['date', 'WeekStatus', 'Day_of_week', 'Appliances', 'rv1', 'rv2']
    drop_cols = [c for c in drop_cols if c in df_appliances.columns]
    
    X_app = df_appliances.drop(columns=drop_cols)
    y_app = df_appliances['Appliances']

    print("Training Appliances Model...")
    X_train_a, X_test_a, y_train_a, y_test_a = train_test_split(X_app, y_app, test_size=0.2, random_state=42)
    # Optimized: n_estimators=10, n_jobs=-1
    clf_appliances = RandomForestRegressor(n_estimators=10, n_jobs=-1, random_state=42)
    clf_appliances.fit(X_train_a, y_train_a)
    joblib.dump(clf_appliances, 'appliances.joblib')
    print("Saved appliances.joblib")

    print("All models retrained and saved.")

if __name__ == "__main__":
    retrain()
