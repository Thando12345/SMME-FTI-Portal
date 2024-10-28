import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv('credit_data.csv')

# Ensure 'credit_score' is present
if 'credit_score' not in data.columns:
    raise ValueError("The dataset must contain a 'credit_score' column.")

# Features and target
X = data.drop('credit_score', axis=1)
y = data['credit_score']

# Print available columns for debugging
print("Available columns in the dataset:", X.columns)

# Define numerical and categorical features
numeric_features = ['age', 'income', 'loan_amount', 'open_accounts', 'credit_history_length', 'savings', 'debt_to_income_ratio']
categorical_features = ['education_level', 'employment_status']

# Identify actual numerical and categorical features in the dataset
numeric_features = [feature for feature in numeric_features if feature in X.columns]
categorical_features = [feature for feature in categorical_features if feature in X.columns]

# Check if there are missing features after filtering
if not numeric_features:
    raise ValueError("No valid numerical features found.")
if not categorical_features:
    raise ValueError("No valid categorical features found.")

print("Numerical features used:", numeric_features)
print("Categorical features used:", categorical_features)

# Preprocessing for numerical features
numeric_transformer = StandardScaler()

# Preprocessing for categorical features
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Create and train the model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train the model
model.fit(X, y)

# Save the model
joblib.dump(model, 'credit_model.pkl')

# Optionally, print the model score on the training set
print("Model R^2 score on training set: ", model.score(X, y))

