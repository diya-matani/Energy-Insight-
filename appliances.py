import sys
import math
import random
import warnings
warnings.filterwarnings("ignore")
from lightgbm import LGBMRegressor
import pandas as pd
import numpy as np
import datetime
import requests
import os
from dotenv import load_dotenv
import google.generativeai as gen_ai
import joblib
from joblib import load
from sklearn.linear_model import SGDRegressor


# Function to start a chat session
def start_chat(g_model):
  chat_session = g_model.start_chat(history=[])
  return chat_session


# Function to process user input and get response
def get_response(user_prompt, chat_session):
  # Send user's message to Gemini-Pro and get the response
  gemini_response = chat_session.send_message(user_prompt)
  return gemini_response.text


def suggestion(pmp):
    load_dotenv()

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # Set up Google Gemini-Pro AI model
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    g_model = gen_ai.GenerativeModel('gemini-pro')

    # Initialize chat session
    chat_session = start_chat(g_model)
    # Get user input
    user_prompt = pmp

    # Get response from Gemini-Pro
    response = get_response(user_prompt, chat_session)

    # Print Gemini-Pro's response
    print(f"Suggestion: {response}")


def predict_appliances(lights, T1, RH_1, T2, RH_2, T3, RH_3, T4, RH_4, T5, RH_5, T6, RH_6, T7, RH_7, T8, RH_8, T9, RH_9, T_out, Press_mm_hg, RH_out, Windspeed, Visibility, Tdewpoint, NSM):
    try:
        # Convert inputs to appropriate data types
        lights = float(lights)
        T1 = float(T1)
        RH_1 = float(RH_1)
        T2 = float(T2)
        RH_2 = float(RH_2)
        T3 = float(T3)
        RH_3 = float(RH_3)
        T4 = float(T4)
        RH_4 = float(RH_4)
        T5 = float(T5)
        RH_5 = float(RH_5)
        T6 = float(T6)
        RH_6 = float(RH_6)
        T7 = float(T7)
        RH_7 = float(RH_7)
        T8 = float(T8)
        RH_8 = float(RH_8)
        T9 = float(T9)
        RH_9 = float(RH_9)
        T_out = float(T_out)
        Press_mm_hg = float(Press_mm_hg)
        RH_out = float(RH_out)
        Windspeed = float(Windspeed)
        Visibility = float(Visibility)
        Tdewpoint = float(Tdewpoint)
        NSM = float(NSM)
    except ValueError as e:
        print(f"Error converting input values: {e}")
        return

    try:
        # Create a dictionary with the user-input data
        new_data = {'lights': [lights], 'T1': [T1], 'RH_1': [RH_1], 'T2': [T2], 'RH_2': [RH_2],
                    'T3': [T3], 'RH_3': [RH_3], 'T4': [T4], 'RH_4': [RH_4], 'T5': [T5], 'RH_5': [RH_5],
                    'T6': [T6], 'RH_6': [RH_6], 'T7': [T7], 'RH_7': [RH_7], 'T8': [T8], 'RH_8': [RH_8],
                    'T9': [T9], 'RH_9': [RH_9], 'T_out': [T_out], 'Press_mm_hg': [Press_mm_hg], 'RH_out': [RH_out],
                    'Windspeed': [Windspeed], 'Visibility': [Visibility], 'Tdewpoint': [Tdewpoint],
                    'NSM': [NSM]}

        # Create a DataFrame with the new data
        new_data_df = pd.DataFrame(data=new_data)

        # Load the pre-trained model
        clf = joblib.load(r'D:\Projects\Energy-Insight\Dump\main\appliances.joblib')

        # Make predictions using the trained model
        prediction = clf.predict(new_data_df)

        print(f"The predicted Appliances value is: {prediction[0]}")
        # pmp = f"i have a Relative Compactness of {X1}, Surface Area of {X2}, Wall Area of {X3}, Roof Area of {X4}, Overall Height of {X5}, Orientation of {X6}, Glazing Area of {X7}, Glazing Area Distribution of {X8}, Overall Width of {ow}, Perimeter of {peri}. Cooling load of {prediction_cool}.  is this a perfect design according to HVAC engineering, suggest me improvements in the above-mentioned categories, so that the temperature in the room is moderate than outside." #and Cooling load of {pred_cool_load}
        pmp = f"Based on Additional relevant features for predicting appliance energy consumption in HVAC engineering include HVAC system status, thermostat setpoints, occupancy data, building characteristics, outdoor weather conditions, HVAC system specifications, and appliance usage patterns. i have lights using {lights} wh energy, {T1} degree celcius with {RH_1} percentage in humidity of the room 1,{T2} degree celcius with {RH_2} percentage in humidity of the room 2, {T3} degree celcius with {RH_3} percentage in humidity of the room 3,{T4} degree celcius with {RH_4} percentage in humidity of the room 4,{T5} degree celcius with {RH_5} percentage in humidity of the room 5,{T6} degree celcius with {RH_6} percentage in humidity of the room 6,{T7} degree celcius with {RH_7} percentage in humidity of the room 7,{T8} degree celcius with {RH_8} percentage in humidity of the room 8,{T9} degree celcius with {RH_9} percentage in humidity of the room 9, {T_out} degree celcius temperature outside, {Press_mm_hg} mm Hg pressure outside, {RH_out} % humidity outside, {Windspeed} metre per second windspeed outside, visibity of {Visibility} kms, {Tdewpoint} 15.00 degree celcius and {NSM} number of seconds from midnight. So is this energy efficient, and what changes i should make or implement to make it energy efficient."
        suggestion(pmp)
    except Exception as e:
        print(f"Error during prediction: {e}")

# Check if the script is being run from the command line
if __name__ == "__main__":
    # Read command-line arguments
    args = sys.argv[1:]

    # Display command-line arguments for debugging
    # print(f"Received arguments: {args}")

    # Check if the correct number of arguments is provided
    if len(args) != 26:
        print("Incorrect number of arguments. Please provide values for all features.")
    else:
        # Call the predict_appliances function with the provided arguments
        predict_appliances(*args)
