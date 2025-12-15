import math
import random
import warnings
warnings.filterwarnings("ignore")
from lightgbm import LGBMRegressor
import pandas as pd
import numpy as np
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split
import datetime
import requests
import os
from dotenv import load_dotenv
import google.generativeai as gen_ai
from joblib import load

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

def get_season(date):
    # Define date ranges for winter and summer seasons
    winter_start = datetime.datetime(date.year, 1, 1)
    winter_end = datetime.datetime(date.year, 4, 1)
    summer_start = datetime.datetime(date.year, 4, 1)
    summer_end = datetime.datetime(date.year, 10, 1)

    # Check if the current date falls within the winter or summer ranges
    if (date >= winter_start and date < winter_end) or (date >= summer_start and date < summer_end):
        return "Winter" if date < winter_end else "Summer"
    else:
        return "Neither Winter nor Summer"

def calculate_dew_point_temperature(temperature, relative_humidity):
    a = 17.27
    b = 237.7
    gamma = (math.log(relative_humidity / 100) + (a * temperature) / (b + temperature)) / \
            ((a * b) / (b + temperature) - math.log(relative_humidity / 100) - 1)
    dew_point_temperature = (b * gamma) / (a - gamma)
    return dew_point_temperature

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
    print(f"Gemini-Pro: {response}")

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = 'ba1b7f5763035389dc83737b7a0e29e5'

# Specify the city for which you want to get weather data
city = input("Enter the city : ")

# Get weather data
weather = get_weather(api_key, city) #weather is diactionary of temp, pressure, humidity, windspeedm, visibiltiy

rc = float(input("Enter Relative Compactness : "))
sa = float(input("Enter the Surface Area : "))
wa = float(input("Enter the wall area : "))
ra = float(input("Enter the Roof Area : "))
ovrh = float(input("Enter the overall height of the wall : "))
orientation  = float(input("Enter the oreintation : "))
ga = float(input("Enter the Glazing area : "))
gad = float(input("Enter the Glazing area distribution : "))
ow = (wa/4)/ovrh
peri = 2*(ovrh + ow)

# cooling load is for SUmmer
# heating load is for winters

# Get current date
current_date = datetime.datetime.now()
# Determine the season
current_season = get_season(current_date)
print("Current season:", current_season)

inp = [[rc, sa, wa, ra, ovrh, orientation, ga, gad, ow, peri]]

if(current_season == "Winter"):
    clf1 = load('heating_load.joblib')
    pred_heat_load = clf1.predict(inp)
    print("The Heating Load is : ",pred_heat_load[0])
    temp_room = weather['temperature'] + pred_heat_load[0]

elif(current_season == "Summer"):
    clf2 = load('cooling_load.joblib')
    pred_cool_load = clf2.predict(inp)
    print("The Cooling Load is : ",pred_cool_load[0])
    temp_room = weather['temperature'] - pred_cool_load[0]


pmp = f"i have a Relative Compactness of {rc}, Surface Area of {sa}, Wall Area of {wa}, Roof Area of {ra}, Overall Height of {ovrh}, Orientation of {orientation}, Glazing Area of {ga}, Glazing Area Distribution of {gad}, Overall Width of {ow}, Perimeter of {peri}. Cooling load of {pred_cool_load}.  is this a perfect design according to HVAC engineering, suggest me improvements in the above-mentioned categories, so that the temperature in the room is moderate than outside." #and Cooling load of {pred_cool_load}

suggestion(pmp)