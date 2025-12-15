# Energy Insight
### [Go to Streamlit](https://energyinsight.streamlit.app/)
**Sustainability Plans: You Make, We Save.**

Energy Insight is a comprehensive Streamlit application designed for building energy analysis. It utilizes machine learning models to predict heating/cooling loads and appliance energy consumption, while integrating real-time weather data and an AI-powered expert assistant.

## Features

- **Home**: Overview of the project and sustainability goals.
- **Weather**: Real-time environmental data (Temperature, Humidity, Wind Speed, etc.) for any city.
- **Building Load**: Predictive analytics for Heating and Cooling loads based on building geometry (Relative Compactness, Surface Area, etc.) using RandomForest regressors.
- **Appliances**: Energy consumption estimation for household appliances based on indoor/outdoor conditions and usage patterns.
- **AI Expert**: An integrated chatbot powered by Google Gemini Pro to provide expert advice on HVAC systems, insulation, and energy-saving strategies.

## Prerequisites

- Python 3.8+
- An [OpenWeatherMap API Key](https://openweathermap.org/api)
- A [Google Gemini API Key](https://ai.google.dev/)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Start-hack/Energy-Insight-.git
    cd Energy-Insight-
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install streamlit pandas numpy scikit-learn joblib requests google-generativeai plotly
    ```

3.  **App Structure:**
    - `app.py`: The main application entry point.
    - `retrain_models.py`: Script to retrain models if you encounter version compatibility issues.
    - `heatLoad.joblib`, `coolLoad.joblib`, `appliance.joblib`: Pre-trained machine learning models.

## Usage

1.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

2.  **Configure API Keys:**
    - Once the app loads, look at the sidebar on the left.
    - Enter your **OpenWeatherMap API Key** and **Google Gemini API Key** to unlock all features.

3.  **Navigate tabs:**
    - Use the top tabs to switch between different modules (Weather, Building Load, Appliances, AI Expert).

## Troubleshooting

- **Model Loading Errors**: If you see errors related to `scikit-learn` version mismatch or pickle files:
    1.  Ensure you have the datasets in `Dump/main/`.
    2.  Run the retraining script:
        ```bash
        python retrain_models.py
        ```
    3.  Restart the Streamlit app.

## License

This project is open-source.
