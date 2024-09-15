import pickle
import streamlit as st

# Load the saved model and feature list
model_path = r'C:\Users\Abhishek\Desktop\Uber_Fare\xgb_model_with_features.pkl'
fare_model = None
features = None

try:
    with open(model_path, 'rb') as file:
        fare_model, features = pickle.load(file)
    st.success("Model and features loaded successfully!")
except FileNotFoundError:
    st.error('Model file not found. Please check the file path.')
except Exception as e:
    st.error(f'Error loading model: {e}')

# Page title
st.title('Fare Amount Prediction using ML')

# Input fields
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    passenger_count = st.text_input('Passenger Count', '1')

with col2:
    distance_km = st.text_input('Distance (km)', '0.0')

with col3:
    month = st.selectbox('Month', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

with col4:
    day_of_week = st.selectbox('Day of Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

with col5:
    # Select box for choosing the time period
    time_period = st.selectbox('Time Period', ['AM Rush', 'Daytime', 'PM Rush', 'Nighttime'])

# Prediction button
if st.button('Predict Fare Amount'):
    if fare_model is None or features is None:
        st.error("Model or features are not loaded. Please check the model file.")
    else:
        try:
            # Convert inputs to numerical values and validate them
            try:
                passenger_count = float(passenger_count)
                distance_km = float(distance_km)
                
                # Validate that distance is greater than 0
                if passenger_count < 0 or distance_km <= 0:
                    raise ValueError("Passenger count must be non-negative and distance must be greater than 0.")
                    
            except ValueError as ve:
                st.error(f'Value Error: {ve}')
                st.stop()

            # Define the expected months and days
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

            # Create month and day mappings
            month_mapping = {m: int(month == m) for m in months}
            day_mapping = {d: int(day_of_week == d) for d in days}

            # Create time period mapping
            time_period_mapping = {
                'AM Rush': 1,
                'Daytime': 2,
                'PM Rush': 3,
                'Nighttime': 4
            }

            # Create input features list
            input_features = [
                passenger_count, distance_km,
                int(time_period == 'AM Rush'),
                int(time_period == 'Daytime'),
                int(time_period == 'PM Rush'),
                int(time_period == 'Nighttime')
            ]
            
            # Extract month and day features based on the model's expected features
            month_features = [month_mapping[m] for m in months if f'month_{m.lower()}' in features]
            day_features = [day_mapping[d] for d in days if f'day_{d.lower()}' in features]

            input_features.extend(month_features)
            input_features.extend(day_features)

            # Ensure the input features length matches the expected length
            if len(input_features) != len(features):
                st.error(f'Feature shape mismatch: Expected {len(features)}, got {len(input_features)}. Features: {features}')
                st.stop()

            fare_prediction = fare_model.predict([input_features])
            st.success(f'Predicted Fare Amount: ${fare_prediction[0]:.2f}')
        except Exception as e:
            st.error(f'An error occurred: {e}')
