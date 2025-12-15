# import sys
# import pandas as pd
# import joblib

# def predict_heat_cool_load(X1, X2, X3, X4, X5, X6, X7, X8):
#     try:
#         # Convert inputs to appropriate data types
#         X1 = float(X1)
#         X2 = float(X2)
#         X3 = float(X3)
#         X4 = float(X4)
#         X5 = float(X5)
#         X6 = float(X6)
#         X7 = float(X7)
#         X8 = float(X8)
#     except ValueError as e:
#         print(f"Error converting input values: {e}")
#         return

#     try:
#         # Create a dictionary with the user-input data
#         new_data = {'X1': [X1], 'X2': [X2], 'X3': [X3], 'X4': [X4],
#                     'X5': [X5], 'X6': [X6], 'X7': [X7], 'X8': [X8]}

#         # Create a DataFrame with the new data
#         new_data_df = pd.DataFrame(data=new_data)

#         # Load the pre-trained models for heating and cooling
#         clf_heat = joblib.load(r'D:\Projects\Energy-Insight\Dump\main\heatLoad.joblib')
#         clf_cool = joblib.load(r'D:\Projects\Energy-Insight\Dump\main\coolLoad.joblib')

#         # Make predictions using the trained models
#         prediction_heat = clf_heat.predict(new_data_df)
#         prediction_cool = clf_cool.predict(new_data_df)

#         print(f"The predicted Heating Load value is: {prediction_heat[0]}")
#         print(f"The predicted Cooling Load value is: {prediction_cool[0]}")

#     except Exception as e:
#         print(f"Error during prediction: {e}")

# # Check if the script is being run from the command line
# if __name__ == "__main__":
#     # Read command-line arguments
#     args_heat_cool = sys.argv[1:]

    
#     # print(f"Received arguments: {args_heat_cool}") # Display command-line arguments for debugging

#     # Check if the correct number of arguments is provided
#     if len(args_heat_cool) != 8:
#         print("Incorrect number of arguments. Please provide values for all features (X1-X8).")
#     else:
#         # Call the predict_heat_cool_load function with the provided arguments
#         predict_heat_cool_load(*args_heat_cool)




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

# Function to start a chat session
def start_chat(g_model):
  chat_session = g_model.start_chat(history=[])
  return chat_session


# Function to process user input and get response
def get_response(user_prompt, chat_session):
    # Send user's message to Gemini-Pro and get the response
    gemini_response = chat_session.send_message(user_prompt)
    
    # Ensure the response text is properly encoded using utf-8
    response_text = gemini_response.text.encode('utf-8', errors='ignore').decode('utf-8')
    
    return response_text


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
    print('\n')
    print(f"\nSuggestion: {response}")


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_data = {
            "temperature": data["main"]["temp"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "windspeed": data["wind"]["speed"],
            "visibility": data.get("visibility", None)
        }
        return weather_data
    else:
        print("Error:", data["message"])

api_key = 'ba1b7f5763035389dc83737b7a0e29e5'

def get_season(date):
    winter_start = datetime.datetime(date.year, 1, 1)
    winter_end = datetime.datetime(date.year, 4, 1)
    summer_start = datetime.datetime(date.year, 4, 1)
    summer_end = datetime.datetime(date.year, 10, 1)

    if (date >= winter_start and date < winter_end) or (date >= summer_start and date < summer_end):
        return "Winter" if date < winter_end else "Summer"
    else:
        return "Neither Winter nor Summer"

def predict_heat_cool_load(city, X1, X2, X3, X4, X5, X6, X7, X8):
    try:
        X1 = float(X1)
        X2 = float(X2)
        X3 = float(X3)
        X4 = float(X4)
        X5 = float(X5)
        X6 = float(X6)
        X7 = float(X7)
        X8 = float(X8)
    except ValueError as e:
        print(f"Error converting input values: {e}")
        return

    try:
        weather_data = get_weather(api_key, city)
        temperature = weather_data["temperature"]
        date = datetime.datetime.now()
        current_season = get_season(date)

        new_data = {'X1': [X1], 'X2': [X2], 'X3': [X3], 'X4': [X4],
                    'X5': [X5], 'X6': [X6], 'X7': [X7], 'X8': [X8]}

        new_data_df = pd.DataFrame(data=new_data)

        # clf_heat = joblib.load(r'D:\Projects\Energy-Insight\Dump\main\heatLoad.joblib')
        clf_heat = joblib.load('heatLoad.joblib')
        # clf_cool = joblib.load(r'D:\Projects\Energy-Insight\Dump\main\coolLoad.joblib')
        clf_cool = joblib.load('coolLoad.joblib')

        prediction_heat = clf_heat.predict(new_data_df)
        prediction_cool = clf_cool.predict(new_data_df)

        ow = (X3/4)/X5
        peri = 2*(X5 + ow)
        if current_season == "Winter":
            prediction_heat += temperature
            print(f"The predicted Heating Load value is: {prediction_heat[0]}\n")
        elif current_season == "Summer":
            prediction_cool -= temperature
            print(f"The predicted Cooling Load value is: {prediction_cool[0]}\n")
            pmp = f"i have a Relative Compactness of {X1}, Surface Area of {X2}, Wall Area of {X3}, Roof Area of {X4}, Overall Height of {X5}, Orientation of {X6}, Glazing Area of {X7}, Glazing Area Distribution of {X8}, Overall Width of {ow}, Perimeter of {peri}. Cooling load of {prediction_cool}.  is this a perfect design according to HVAC engineering, suggest me improvements in the above-mentioned categories, so that the temperature in the room is moderate than outside." #and Cooling load of {pred_cool_load}
            suggestion(pmp)


    except Exception as e:
        print(f"Error during prediction: {e}")

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 9:
        print("Incorrect number of arguments. Please provide City, and values for all features (X1-X8).")
    else:
        city = args[0]
        X1, X2, X3, X4, X5, X6, X7, X8 = args[1:]
        predict_heat_cool_load(city, X1, X2, X3, X4, X5, X6, X7, X8)
