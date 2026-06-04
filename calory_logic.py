import joblib
import os
import pandas as pd

# Get the base directory where the executable is running
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load the trained model and scaler using relative paths
best_xgb_model_path = os.path.join(base_dir, 'best_xgb_model.pkl')
scaler_path = os.path.join(base_dir, 'scaler.pkl')

best_xgb_model = joblib.load(best_xgb_model_path)
scaler = joblib.load(scaler_path)

# List of all features used during scaler fitting
all_features = ['Gender', 'age', 'weight', 'height', 'frequencies', 'distance', 'bmi', 'time']

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def predict_calories(weight, height, distance, time, bmi):
    """
    Predict calories burned based on input features using the trained best XGBoost model.
    Ensure the correct order of features and include feature names.
    """
    # Create a dictionary of the input features with default values for missing features
    input_dict = {
        'Gender': 0,  # Default value for gender (e.g., 0 for female, 1 for male)
        'age': 25,    # Default value for age
        'weight': weight,
        'height': height,
        'frequencies': 3,  # Default value for frequencies
        'distance': distance,
        'bmi': bmi,
        'time': time
    }

    # Create a DataFrame of the input features with the correct order
    input_features = pd.DataFrame([input_dict], columns=all_features)

    # Scale the features using all features
    input_features_scaled = scaler.transform(input_features)

    # Predict calories burned
    calories_burned = best_xgb_model.predict(input_features_scaled)[0]
    
    return calories_burned
