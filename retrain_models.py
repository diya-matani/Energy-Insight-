import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def retrain():
    print("Starting model retraining...")
    
    # Paths
    enb_path = os.path.join("Dump", "main", "ENB2012_data.csv")
    training_path = os.path.join("Dump", "main", "training.csv")
    
    # ---------------- Building Load Models ----------------
    if os.path.exists(enb_path):
        print(f"Loading {enb_path}...")
        df_enb = pd.read_csv(enb_path)
        
        # Features X1 to X8
        X_enb = df_enb[['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']]
        y_heat = df_enb['Y1']
        y_cool = df_enb['Y2']
        
        print("Training Heat Load Model...")
        rf_heat = RandomForestRegressor(n_estimators=100, random_state=42)
        rf_heat.fit(X_enb, y_heat)
        joblib.dump(rf_heat, 'heatLoad.joblib')
        print("Saved heatLoad.joblib")
        
        print("Training Cool Load Model...")
        rf_cool = RandomForestRegressor(n_estimators=100, random_state=42)
        rf_cool.fit(X_enb, y_cool)
        joblib.dump(rf_cool, 'coolLoad.joblib')
        print("Saved coolLoad.joblib")
        
    else:
        print(f"Error: {enb_path} not found.")

    # ---------------- Appliance Model ----------------
    if os.path.exists(training_path):
        print(f"Loading {training_path}...")
        df_train = pd.read_csv(training_path)
        
        # Target
        y_app = df_train['Appliances']
        
        # Drop non-feature columns
        # We need to match the feature list expected by app.py:
        # lights, T1, RH_1, ..., Tdewpoint, NSM
        
        # Current columns in CSV (based on inspection):
        # date, Appliances, lights, T1...Tdewpoint, rv1, rv2, NSM, WeekStatus, Day_of_week
        
        features = [
            'lights', 'T1', 'RH_1', 'T2', 'RH_2', 'T3', 'RH_3', 'T4', 'RH_4', 'T5', 'RH_5',
            'T6', 'RH_6', 'T7', 'RH_7', 'T8', 'RH_8', 'T9', 'RH_9', 'T_out', 'Press_mm_hg',
            'RH_out', 'Windspeed', 'Visibility', 'Tdewpoint', 'NSM'
        ]
        
        X_app = df_train[features]
        
        print("Training Appliances Model...")
        rf_app = RandomForestRegressor(n_estimators=100, random_state=42)
        rf_app.fit(X_app, y_app)
        
        # Note: saving as 'appliance.joblib' to match app.py expectation (singular)
        joblib.dump(rf_app, 'appliance.joblib')
        print("Saved appliance.joblib")
        
    else:
        print(f"Error: {training_path} not found.")

    print("Retraining complete.")

if __name__ == "__main__":
    retrain()
