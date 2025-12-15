import streamlit as st
import joblib
import pandas as pd

# Load the trained models
clf_heat = joblib.load('heatLoad.joblib')
clf_cool = joblib.load('coolLoad.joblib')
clf_appliances = joblib.load('appliances.joblib')

# Define the function for making predictions
def predict_heat_cool_load(relative_compactness, surface_area, wall_area, roof_area,
                           overall_height, orientation, glazing_area, glazing_area_distribution):

    # Create a DataFrame with the user-input data
    new_data = {'X1': [relative_compactness], 'X2': [surface_area],
                'X3': [wall_area], 'X4': [roof_area], 'X5': [overall_height],
                'X6': [orientation], 'X7': [glazing_area],
                'X8': [glazing_area_distribution]}

    # Create a DataFrame with the new data
    new_data_df = pd.DataFrame(data=new_data)

    # Make predictions using the trained models
    prediction_heat = clf_heat.predict(new_data_df)
    prediction_cool = clf_cool.predict(new_data_df)

    return prediction_heat[0], prediction_cool[0]

# Create the Streamlit web app
def main():
    # Add header with logo
    # st.image('logo.jpg', width=100)
    st.title("Heating and Cooling Load Prediction")

    # Navigation
    nav_selection = st.radio("Navigation", ["Home", "Appliances"])

    if nav_selection == "Home":
        # Get user input for features
        relative_compactness = st.number_input("Enter Relative Compactness (X1): ")
        surface_area = st.number_input("Enter Surface Area (X2): ")
        wall_area = st.number_input("Enter Wall Area (X3): ")
        roof_area = st.number_input("Enter Roof Area (X4): ")
        overall_height = st.number_input("Enter Overall Height (X5): ")
        orientation = st.number_input("Enter Orientation (X6): ")
        glazing_area = st.number_input("Enter Glazing Area (X7): ")
        glazing_area_distribution = st.number_input("Enter Glazing Area Distribution (X8): ")

        if st.button("Predict"):
            # Call the prediction function for heating and cooling load
            heat_load, cool_load = predict_heat_cool_load(relative_compactness, surface_area, wall_area,
                                                          roof_area, overall_height, orientation,
                                                          glazing_area, glazing_area_distribution)
            st.success(f"The predicted Heating Load value is: {heat_load}")
            st.success(f"The predicted Cooling Load value is: {cool_load}")

    elif nav_selection == "Appliances":
        st.title("Appliance Energy Consumption Prediction")
        # Get user input for appliance features
        lights = st.number_input("Energy use of light fixtures in the house (Wh)", value=0.0)
        T1 = st.number_input("Temperature in kitchen area (°C)")
        RH_1 = st.number_input("Humidity in kitchen area (%)")
        T2 = st.number_input("Temperature in living room area (°C)")
        RH_2 = st.number_input("Humidity in living room area (%)")
        T3 = st.number_input("Temperature in laundry room area (°C)")
        RH_3 = st.number_input("Humidity in laundry room area (%)")
        T4 = st.number_input("Temperature in office room (°C)")
        RH_4 = st.number_input("Humidity in office room (%)")
        T5 = st.number_input("Temperature in bathroom area (°C)")
        RH_5 = st.number_input("Humidity in bathroom area (%)")
        T6 = st.number_input("Temperature outside the building (°C)")
        RH_6 = st.number_input("Humidity outside the building (%)")
        T7 = st.number_input("Temperature in ironing room (°C)")
        RH_7 = st.number_input("Humidity in ironing room (%)")
        T8 = st.number_input("Temperature in teenager room (°C)")
        RH_8 = st.number_input("Humidity in teenager room (%)")
        T9 = st.number_input("Temperature in parent room (°C)")
        RH_9 = st.number_input("Humidity in parent room (%)")
        T_out = st.number_input("Outdoor temperature (°C)")
        Press_mm_hg = st.number_input("Pressure (mm Hg)")
        RH_out = st.number_input("Outdoor humidity (%)")
        Windspeed = st.number_input("Wind speed (m/s)")
        Visibility = st.number_input("Visibility (km)")
        Tdewpoint = st.number_input("Dew point temperature (°C)")
        NSM = st.number_input("Number of seconds since midnight")

        if st.button("Predict"):
            # Call the prediction function for appliances
            prediction = clf_appliances.predict([[lights, T1, RH_1, T2, RH_2, T3, RH_3, T4, RH_4, T5, RH_5,
                                                   T6, RH_6, T7, RH_7, T8, RH_8, T9, RH_9, T_out, Press_mm_hg,
                                                   RH_out, Windspeed, Visibility, Tdewpoint, NSM]])
            st.success(f"The predicted Appliances value is: {prediction[0]:.2f}")

# Run the app
if __name__ == '__main__':
    main()
