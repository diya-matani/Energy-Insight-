import streamlit as st
import joblib
import pandas as pd

# Load the trained model
clf = joblib.load(r'D:\Projects\Energy-Insight\Dump\main\appliances.joblib')

# Define the function for making predictions
def predict_appliances(date, lights, T1, RH_1, T2, RH_2, T3, RH_3, T4, RH_4, T5, RH_5,
                       T6, RH_6, T7, RH_7, T8, RH_8, T9, RH_9, T_out, Press_mm_hg, RH_out,
                       Windspeed, Visibility, Tdewpoint, NSM):

    # Create a DataFrame with the user-input data
    new_data = {'lights': [lights], 'T1': [T1], 'RH_1': [RH_1], 'T2': [T2], 'RH_2': [RH_2],
                'T3': [T3], 'RH_3': [RH_3], 'T4': [T4], 'RH_4': [RH_4], 'T5': [T5], 'RH_5': [RH_5],
                'T6': [T6], 'RH_6': [RH_6], 'T7': [T7], 'RH_7': [RH_7], 'T8': [T8], 'RH_8': [RH_8],
                'T9': [T9], 'RH_9': [RH_9], 'T_out': [T_out], 'Press_mm_hg': [Press_mm_hg], 'RH_out': [RH_out],
                'Windspeed': [Windspeed], 'Visibility': [Visibility], 'Tdewpoint': [Tdewpoint],
                'NSM': [NSM]}

    # Create a DataFrame with the new data
    new_data_df = pd.DataFrame(data=new_data)

    # Make predictions using the trained model
    prediction = clf.predict(new_data_df)

    return prediction[0]

# Create the Streamlit web app
def main():
    st.title("Appliance Energy Consumption Prediction")

    # Get user input for features
    lights = st.number_input("Energy use of light fixtures in the house (Wh)", value=0.0)
    T1 = st.number_input("Temperature in kitchen area (°C)")
    RH_1 = st.number_input("Humidity in kitchen area (%)")
    T2 = st.number_input("Temperature in living room area (°C)")
    RH_2 = st.number_input("Humidity in living room area (%)")
    T3 = st.number_input("Temperature in laundry room area (°C)")
    RH_3 = st.number_input("Humidity in laundry room area (%)")
    # Add more input fields for other features

    if st.button("Predict"):
        # Call the prediction function
        prediction = predict_appliances(lights, T1, RH_1, T2, RH_2, T3, RH_3)  # Add more features here
        st.success(f"The predicted Appliances value is: {prediction:.2f}")

# Run the app
if __name__ == '__main__':
    main()
