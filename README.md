# Uber Fare Amount Prediction App

This repository contains a Streamlit app for predicting Uber fare amounts based on user input using a machine learning model. The app is designed to provide fare predictions based on various features including passenger count, distance, month, day of the week, and time period of the day.

## Project Structure

- `app.py`: The main Streamlit application script that serves as the user interface for the fare prediction.
- `model_training_notebook.ipynb`: Jupyter notebook used for training the machine learning model. It includes data preparation, model training, and saving the model.
- `xgb_model_with_features.pkl`: Pickle file containing the trained model and feature list. Ensure this file is available in the specified directory or adjust the path in `app.py`.

## Features

- **Passenger Count**: Input the number of passengers.
- **Distance (km)**: Input the distance traveled in kilometers.
- **Month**: Select the month of the ride.
- **Day of Week**: Select the day of the week.
- **Time Period**: Select the time period (AM Rush, Daytime, PM Rush, Nighttime).

## Requirements

- Python 3.7 or later
- Streamlit
- Scikit-learn (for the machine learning model)
- Pickle (for loading the model)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/uber_fare_prediction.git
    cd uber_fare_prediction
    ```


2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure the model file is in the correct directory:**

    Place the `xgb_model_with_features.pkl` file in the  directory or update the `model_path` variable in `app.py` with the correct path to your model file.

## Running the App

To run the Streamlit app, use the following command:

```bash
streamlit run app.py
