import streamlit as st
import joblib
import pandas as pd
import numpy as np
import requests
import google.generativeai as gen_ai
import plotly.graph_objects as go
import plotly.express as px
import os

# Set page config
st.set_page_config(
    page_title="Energy Insight",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern look
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    div.stButton > button:first-child {
        background-color: #2ecc71;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #27ae60;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- Helper Functions -----------------
@st.cache_resource
def load_models():
    try:
        clf_heat = joblib.load('heatLoad.joblib')
        clf_cool = joblib.load('coolLoad.joblib')
        # Corrected filename from appliances.joblib to appliance.joblib
        clf_appliances = joblib.load('appliance.joblib')
        return clf_heat, clf_cool, clf_appliances
    except FileNotFoundError as e:
        st.error(f"Model file not found: {e}")
        return None, None, None
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None, None

def get_weather(api_key, city):
    if not api_key:
        return None
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error fetching weather: {response.json().get('message', 'Unknown error')}")
            return None
    except Exception as e:
        st.error(f"Connection error: {e}")
        return None

def start_chat(api_key):
    if not api_key:
        return None
    try:
        gen_ai.configure(api_key=api_key)
        model = gen_ai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])
        return chat
    except Exception as e:
        st.error(f"Gemini API Error: {e}")
        return None

# ----------------- Main App -----------------
def main():
    # Sidebar
    with st.sidebar:
        st.title("Configuration")
        st.markdown("---")
        
        # API Keys
        st.subheader("API Keys")
        weather_api_key = st.text_input("OpenWeatherMap API Key", type="password", help="Required for Weather tab")
        gemini_api_key = st.text_input("Google Gemini API Key", type="password", help="Required for AI Expert tab")
        
        st.markdown("---")
        st.markdown("### About")
        with st.expander("About this App"):
            st.markdown("""
            **Energy Insight** is a comprehensive tool for building energy analysis.
            
            - **Author**: Energy Insight Team
            - **Version**: 2.0
            - **Powered by**: Streamlit, Scikit-learn, Gemini Pro
            """)
        st.info("Navigate using the tabs above.")

    # Load Models
    clf_heat, clf_cool, clf_appliances = load_models()
    if not clf_heat:
        st.stop()

    # Main Content
    st.markdown('<div class="main-header">Energy Insight</div>', unsafe_allow_html=True)
    
    # Tabs
    tab_home, tab_weather, tab_load, tab_appliances, tab_ai = st.tabs([
        "Home", "Weather", "Building Load", "Appliances", "AI Expert"
    ])

    # --- HOME TAB ---
    with tab_home:
        st.markdown("### Welcome to Energy Insight")
        st.markdown("""
        **Sustainability Plans: You Make, We Save.**
        
        This application provides advanced predictive analytics for building efficiency.
        
        **Features:**
        - **Weather Integration**: Real-time environmental data.
        - **Heat & Cool Load Prediction**: Optimize your HVAC system based on building geometry.
        - **Appliance Energy Prediction**: Estimate energy consumption based on usage and environment.
        - **AI Energy Expert**: Get personalized advice from our AI assistant.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
             st.info("Please enter your API keys in the sidebar to unlock all features.")
        with col2:
             st.image("https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", use_column_width=True)


    # --- WEATHER TAB ---
    with tab_weather:
        st.markdown("### Real-Time Weather Data")
        city = st.text_input("Enter City Name", "London")
        if st.button("Get Weather"):
            if weather_api_key:
                weather_data = get_weather(weather_api_key, city)
                if weather_data:
                    main_data = weather_data['main']
                    wind_data = weather_data['wind']
                    
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Temperature", f"{main_data['temp']} °C")
                    c2.metric("Humidity", f"{main_data['humidity']} %")
                    c3.metric("Pressure", f"{main_data['pressure']} hPa")
                    
                    c4, c5 = st.columns(2)
                    c4.metric("Wind Speed", f"{wind_data['speed']} m/s")
                    c5.metric("Description", weather_data['weather'][0]['description'].title())
            else:
                st.warning("Please enter OpenWeatherMap API Key in sidebar.")

    # --- BUILDING LOAD TAB ---
    with tab_load:
        st.markdown("### Predict Heating & Cooling Loads")
        st.write("Enter building parameters to estimate loads.")
        
        with st.form("load_form"):
            c1, c2 = st.columns(2)
            with c1:
                rc = st.number_input("Relative Compactness", 0.0, 1.0, 0.74, help="Ratio of building surface area to volume.")
                sa = st.number_input("Surface Area", 500.0, 850.0, 686.0, help="Total surface area of the building.")
                wa = st.number_input("Wall Area", 200.0, 450.0, 245.0, help="Total wall area.")
                ra = st.number_input("Roof Area", 100.0, 250.0, 220.5, help="Total roof area.")
            with c2:
                oh = st.number_input("Overall Height", 3.0, 10.0, 3.5, help="Height of the building.")
                orient = st.selectbox("Orientation", [2, 3, 4, 5], index=0, help="Building orientation (2=North, 3=East, 4=South, 5=West).")
                ga = st.number_input("Glazing Area", 0.0, 0.4, 0.1, help="Proportion of floor area as glazing.")
                gad = st.selectbox("Glazing Area Dist.", [0, 1, 2, 3, 4, 5], index=1, help="Distribution of glazing.")
                
            submitted = st.form_submit_button("Predict Loads")
            
            if submitted:
                # Feature Engineering
                # X9: Overall Width
                x9 = (wa / 4) / oh
                # X10: Perimeter
                x10 = 2 * (oh + x9)

                input_data = pd.DataFrame({
                    'X1':[rc], 'X2':[sa], 'X3':[wa], 'X4':[ra], 
                    'X5':[oh], 'X6':[orient], 'X7':[ga], 'X8':[gad],
                    'X9':[x9], 'X10':[x10]
                })
                
                heat_pred = clf_heat.predict(input_data)[0]
                cool_pred = clf_cool.predict(input_data)[0]
                
                res1, res2 = st.columns(2)
                res1.metric("Heating Load", f"{heat_pred:.2f} kWh")
                res2.metric("Cooling Load", f"{cool_pred:.2f} kWh")
                
                # Plotly Chart
                fig = go.Figure(data=[
                    go.Bar(name='Heating Load', x=['Load'], y=[heat_pred], marker_color='#ff6b6b'),
                    go.Bar(name='Cooling Load', x=['Load'], y=[cool_pred], marker_color='#4ecdc4')
                ])
                fig.update_layout(barmode='group', title_text='Projected Energy Loads', height=400)
                st.plotly_chart(fig, use_container_width=True)

    # --- APPLIANCES TAB ---
    with tab_appliances:
        st.markdown("### Appliance Energy Consumption")
        st.write("Predict energy use based on comprehensive sensor data.")
        
        with st.form("appliance_form"):
            with st.expander("Indoor Conditions (Kitchen & Living)", expanded=True):
                c1, c2, c3 = st.columns(3)
                T1 = c1.number_input("Kitchen Temp (°C)", 20.0, help="Temp in kitchen area")
                RH_1 = c1.number_input("Kitchen Hum (%)", 40.0, help="Humidity in kitchen area")
                T2 = c2.number_input("Living Room Temp", 19.0)
                RH_2 = c2.number_input("Living Room Hum", 40.0)
                T3 = c3.number_input("Laundry Temp", 20.0)
                RH_3 = c3.number_input("Laundry Hum", 40.0)
                
            with st.expander("Other Rooms (Office, Bath, Ironing)"):
                c1, c2, c3 = st.columns(3)
                T4 = c1.number_input("Office Temp", 20.0)
                RH_4 = c1.number_input("Office Hum", 40.0)
                T5 = c2.number_input("Bath Temp", 19.0)
                RH_5 = c2.number_input("Bath Hum", 45.0)
                T7 = c3.number_input("Ironing Temp", 18.0)
                RH_7 = c3.number_input("Ironing Hum", 35.0)

            with st.expander("Private Rooms (Teen & Parent)"):
                c1, c2 = st.columns(2)
                T8 = c1.number_input("Teen Room Temp", 20.0)
                RH_8 = c1.number_input("Teen Room Hum", 42.0)
                T9 = c2.number_input("Parent Room Temp", 19.0)
                RH_9 = c2.number_input("Parent Room Hum", 40.0)

            with st.expander("Outdoor & Weather"):
                c1, c2, c3 = st.columns(3)
                T6 = c1.number_input("Outside (North)", 5.0, help="Temp outside (north side)")
                RH_6 = c1.number_input("Outside Hum (North)", 80.0)
                T_out = c2.number_input("Chievres Station Temp", 4.0, help="Temp from weather station")
                RH_out = c2.number_input("Chievres Hum", 80.0)
                Press_mm_hg = c3.number_input("Pressure (mm Hg)", 760.0)
                Windspeed = c3.number_input("Windspeed (m/s)", 3.0)
                Visibility = c1.number_input("Visibility (km)", 40.0)
                Tdewpoint = c2.number_input("Dew Point (°C)", 2.0)

            with st.expander("Other Factors"):
                c1, c2 = st.columns(2)
                lights = c1.number_input("Lights (Wh)", 0.0, help="Energy use of light fixtures")
                NSM = c2.number_input("Seconds from Midnight", 0, help="Number of seconds elapsed from midnight")

            app_submit = st.form_submit_button("Predict Consumption")
            
            if app_submit:
                # Construct input array in correct order
                features = [[lights, T1, RH_1, T2, RH_2, T3, RH_3, T4, RH_4, T5, RH_5, 
                             T6, RH_6, T7, RH_7, T8, RH_8, T9, RH_9, T_out, Press_mm_hg, 
                             RH_out, Windspeed, Visibility, Tdewpoint, NSM]]
                
                app_pred = clf_appliances.predict(features)[0]
                
                st.divider()
                st.success(f"Predicted Energy Consumption: {app_pred:.2f} Wh")
                
                # Gauge Chart
                fig = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = app_pred,
                    title = {'text': "Appliance Consumption (Wh)"},
                    gauge = {
                        'axis': {'range': [None, 300]}, # Assuming 200-300 is high based on typical appliance data
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [0, 50], 'color': "lightgreen"},
                            {'range': [50, 150], 'color': "yellow"},
                            {'range': [150, 300], 'color': "red"}],
                    }
                ))
                st.plotly_chart(fig, use_container_width=True)

    # --- AI EXPERT TAB ---
    with tab_ai:
        st.markdown("### AI Energy Expert")
        st.write("Ask Gemini for advice on improving energy efficiency.")
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        if gemini_api_key:
             # Display chat history
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("Ask about HVAC, insulation, or energy saving..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    # Improve prompt with context
                    system_prompt = "You are an expert in Building Energy Efficiency, HVAC systems, and sustainable living. Provide helpful, concise advice."
                    full_prompt = f"{system_prompt}\nUser asked: {prompt}"
                    
                    chat = start_chat(gemini_api_key)
                    if chat:
                        try:
                            response = chat.send_message(full_prompt)
                            st.markdown(response.text)
                            st.session_state.messages.append({"role": "assistant", "content": response.text})
                        except Exception as e:
                            st.error(f"Error: {e}")
        else:
            st.warning("Please enter your Google Gemini API Key in the sidebar to use the AI chat.")

if __name__ == "__main__":
    main()
