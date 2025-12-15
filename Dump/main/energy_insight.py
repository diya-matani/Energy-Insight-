import math
import random
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split
import datetime
import requests
import os
from dotenv import load_dotenv
import google.generativeai as gen_ai

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

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = 'xyz'

# Specify the city for which you want to get weather data
city = input("Enter the city : ")

# Get weather data
weather = get_weather(api_key, city) #weather is diactionary of temp, pressure, humidity, windspeedm, visibiltiy

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

# feature engineering

df = pd.read_csv("ENB2012_data.csv")
# new feature
df['X9'] = (df['X3']/4)/df['X5']
df['X10'] = 2 * (df['X5'] + df['X9'])

# multiclass data distribution

X = df.drop(columns=['Y1','Y2'])
y1 = df['Y1']
y2 = df['Y2']
X_train, X_test, y_train, y_test = train_test_split(X,y1, test_size = 0.2, random_state = 42)
clf1 = RandomForestRegressor().fit(X_train, y_train) #heating load
y_pred_1 = clf1.predict(X_test)

X_train, X_test, y_train, y_test = train_test_split(X,y2, test_size = 0.2, random_state = 42)
clf2 = RandomForestRegressor().fit(X_train, y_train) # cooling load
y_pred_2 = clf2.predict(X_test)

# predicting value
n = 9 # Number of rooms in a building
outer = []
inner = [random.randint(0, 51)]

for i in range(n) :
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
        pred_heat_load = clf1.predict(inp)
        print("The Heating Load is : ",pred_heat_load[0])
        temp_room = weather['temperature'] + pred_heat_load[0]

    elif(current_season == "Summer"):
        pred_cool_load = clf2.predict(inp)
        print("The Cooling Load is : ",pred_cool_load[0])
        temp_room = weather['temperature'] - pred_cool_load[0]


    pmp = f"i have a Relative Compactness of {rc}, Surface Area of {sa}, Wall Area of {wa}, Roof Area of {ra}, Overall Height of {ovrh}, Orientation of {orientation}, Glazing Area of {ga}, Glazing Area Distribution of {gad}, Overall Width of {ow}, Perimeter of {peri}. Heating load of {pred_heat_load}.  is this a perfect design according to HVAC engineering, suggest me improvements in the above-mentioned categories, so that the temperature in the room is moderate than outside." #and Cooling load of {pred_cool_load}

    suggestion(pmp)

    humidity = weather['humidity']
    inner.append(temp_room)
    inner.append(humidity)

temp_out = weather['temperature']
pressure = weather['pressure']
humidity = weather['humidity']
wind_speed = weather['windspeed']
visibility = weather['visibility']
dew_point = calculate_dew_point_temperature(temp_out, humidity)
inner.append(temp_out)
inner.append(pressure)
inner.append(humidity)
inner.append(wind_speed)
inner.append(visibility)
inner.append(dew_point)
inner.append(random.randint(0, 85801))
outer.append(inner)

print(outer)

# outer = [[40, 44.92579999999998, 13, 53.01569999999999, 13, 37.04790000000001, 13, 61.7384, 13, 39.594300000000004, 13, 43.70270000000002, 13, 64.73680000000004, 13, 52.81220000000003, 13, 61.17279999999998, 13, 28.45, 1012, 13, 2.73, 10000, -0.16219615879054802, 84757]]

# dataset-2
df_train = pd.read_csv("training.csv")
df_train = df_train.drop(columns=['date','WeekStatus','Day_of_week'])
X = df_train.drop(columns=['Appliances','rv1','rv2'])
y = df_train['Appliances']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)
print("processing...")
clf = RandomForestRegressor().fit(X_train, y_train)
print("processed.")
y_pred = clf.predict(X_test)
y_pred_2 = clf.predict(outer)
error = root_mean_squared_error(y_test, y_pred)
print(y_pred_2[0], "wh")



# suggestionn

# Load environment variables




