import pickle
import streamlit as st

# Load the saved model
model_path = 'xgb.pkl'
try:
    fare_model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    st.error('Model file not found. Please check the file path.')

# Page title
st.title('Fare Amount Prediction using ML')

# Input fields
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

with col1:
    passenger_count = st.text_input('Passenger Count', '1')

with col2:
    distance_km = st.text_input('Distance (km)', '0.0')

with col3:
    am_rush = st.selectbox('AM Rush (0/1)', [0, 1])

with col4:
    daytime = st.selectbox('Daytime (0/1)', [0, 1])

with col5:
    pm_rush = st.selectbox('PM Rush (0/1)', [0, 1])

with col6:
    nighttime = st.selectbox('Nighttime (0/1)', [0, 1])

with col7:
    month = st.selectbox('Month', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

with col8:
    day_of_week = st.selectbox('Day of Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Default value for fare_prediction
fare_prediction = ''

# Prediction button
if st.button('Predict Fare Amount'):
    # Ensure input data is valid and convert to appropriate types
    try:
        # Convert month and day of week to one-hot encoding
        month_mapping = {month: int(month == m) for m in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
        day_mapping = {day: int(day == d) for d in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
        
        input_data = [
            float(passenger_count), float(distance_km),
            int(am_rush), int(daytime),
            int(pm_rush), int(nighttime),
            month_mapping[month],
            day_mapping[day_of_week]
        ]
        
        # Ensure input data matches the model's expected input shape
        input_data = [input_data + [0] * (23 - len(input_data))]  # Adjust size as needed

        fare_prediction = fare_model.predict(input_data)
        st.success(f'Predicted Fare Amount: ${fare_prediction[0]:.2f}')
    except ValueError:
        st.error('Please enter valid numerical values for all input fields.')
    except Exception as e:
        st.error(f'An error occurred: {e}')

# Display the prediction result
if fare_prediction:
    st.success(f'Predicted Fare Amount: ${fare_prediction[0]:.2f}')
