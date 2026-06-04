

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from xgboost import XGBRegressor, plot_importance
from sklearn.impute import SimpleImputer
import pickle

# Load and preprocess dataset
df = pd.read_csv('Calorie.csv')
print("Data loaded successfully.")
print(df.head())

# Check for missing values
print("Missing values in each column:\n", df.isnull().sum())

# Encode categorical variable 'Gender'
df['Gender'] = df['Gender'].map({'male': 1, 'female': 0})

# Impute missing values using median
imputer = SimpleImputer(strategy='median')
df[['age', 'weight', 'height', 'frequencies', 'distance', 'bmi', 'time']] = imputer.fit_transform(df[['age', 'weight', 'height', 'frequencies', 'distance', 'bmi', 'time']])

# Check again for missing values after imputation
print("Missing values after imputation:\n", df.isnull().sum())

# Features and target variable
X = df[['Gender', 'age', 'weight', 'height', 'frequencies', 'distance', 'bmi', 'time']]
y = df['calories']

# Scale the features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# XGBoost Regressor
xgb_model = XGBRegressor(random_state=42)

# Hyperparameter tuning
param_grid = {
    'n_estimators': np.arange(100, 500, 100),
    'max_depth': np.arange(3, 10),
    'learning_rate': [0.01, 0.2, 0.4, 0.6],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0]
}

grid_search_xgb = GridSearchCV(
    xgb_model, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1, verbose=1
)
grid_search_xgb.fit(X_train, y_train)

# Best hyperparameters and model
best_xgb_model = grid_search_xgb.best_estimator_
print("Best Hyperparameters (XGBoost GridSearch):", grid_search_xgb.best_params_)
print("Best CV Score (XGBoost GridSearch):", -grid_search_xgb.best_score_)

# Model training
best_xgb_model.fit(X_train, y_train)
y_pred_xgb = best_xgb_model.predict(X_test)

# Performance metrics
mae_xgb = mean_absolute_error(y_test, y_pred_xgb)
mse_xgb = mean_squared_error(y_test, y_pred_xgb)
rmse_xgb = np.sqrt(mse_xgb)  # Calculate the root mean squared error
r2_xgb = r2_score(y_test, y_pred_xgb)
print(f'XGBoost Regressor MAE: {mae_xgb:.4f}, MSE: {mse_xgb:.4f}, RMSE:{rmse_xgb:.4f}, R²: {r2_xgb:.4f}')

# Save the best XGBoost model and the scaler
with open('best_xgb_model.pkl', 'wb') as model_file:
    pickle.dump(best_xgb_model, model_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

# Feature importance plot
plt.figure(figsize=(10, 8))
plot_importance(best_xgb_model)
plt.title('XGBoost Feature Importance')
plt.show()

# --- NEW PREDICTION FUNCTION ---
def predict_calories(new_data_input):
    """
    Predicts calorie burn using the trained XGBoost model.

    Args:
        new_data_input (pd.DataFrame): DataFrame with new data. Must include all columns
        'Gender', 'age', 'weight', 'height', 'frequencies', 'distance', 'bmi', 'time'
         in the correct order.

    Returns:
         np.ndarray: The predictions with the XGBoost model.
    """
    # Ensure new data has the same columns as X
    new_data_input = new_data_input[X.columns]

    # Scale the input data
    new_data_scaled_input = scaler.transform(new_data_input)

    # Load the saved XGBoost model
    with open('best_xgb_model.pkl', 'rb') as model_file:
        loaded_xgb_model = pickle.load(model_file)

    # Make predictions with the XGBoost model
    predictions_best_xgb_input = loaded_xgb_model.predict(new_data_scaled_input)

    return predictions_best_xgb_input

# Example usage of the new function
new_data_example = pd.DataFrame({
    'Gender': [0, 1],
    'age': [25, 22],
    'weight': [80, 60],
    'height': [175, 165],
    'frequencies': [2, 5],
    'distance': [10, 5],
    'bmi': [25, 21],
    'time': [1, 2]
})

predictions_xgb = predict_calories(new_data_example)
print("Predictions using Best XGBoost model:\n", predictions_xgb)
