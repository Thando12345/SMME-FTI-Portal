import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load the dataset
data_path = r'C:\Users\CASH CRUSADERS NORTH\OneDrive - Networx for Career Development\Desktop\SMME-FTI-Portal\credit_data.csv'
data = pd.read_csv(data_path)

# Preprocessing
X = data.drop(columns=['credit_score'])  # Features
y = data['credit_score']  # Target variable

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'credit_model.pkl')
