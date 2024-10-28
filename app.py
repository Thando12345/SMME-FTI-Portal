import os
from flask import Flask, request, render_template, redirect, url_for, flash
import pandas as pd
import joblib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Define paths for your model and uploads
MODEL_PATH = r'C:\Users\CASH CRUSADERS NORTH\OneDrive - Networx for Career Development\Desktop\SMME-FTI-Portal\credit_model.pkl'
UPLOAD_FOLDER = r'C:\Users\CASH CRUSADERS NORTH\OneDrive - Networx for Career Development\Desktop\SMME-FTI-Portal\uploads'

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load your trained model
model = joblib.load(MODEL_PATH)

# Function to preprocess the data and predict credit scores
def predict_credit_scores(file_path):
    # Load the CSV data
    data = pd.read_csv(file_path)

    # Define features used for prediction
    features = [
        'age', 'income', 'loan_amount', 'open_accounts', 
        'credit_history_length', 'defaulted_before', 
        'education_level', 'employment_status', 
        'savings', 'debt_to_income_ratio'
    ]
    
    # Check if all features are present in the uploaded data
    if not all(feature in data.columns for feature in features):
        raise ValueError("Uploaded file is missing required features.")
    
    # Extract features from the data
    X = data[features]

    # Check for NaN values in the features
    if X.isnull().values.any():
        raise ValueError("Input data contains NaN values. Please clean your data before uploading.")

    # Make predictions using the model
    credit_scores = model.predict(X)
    
    # Add the predictions to the DataFrame
    data['predicted_credit_score'] = credit_scores
    return data

@app.route('/')
def index():
    # Render the index page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the request contains a file
    if 'file' not in request.files:
        flash("No file part in request", "danger")
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    # Check if a valid file was selected
    if file.filename == '':
        flash("No file selected", "danger")
        return redirect(url_for('index'))

    # Validate file extension
    if not file.filename.endswith('.csv'):
        flash("Only CSV files are accepted", "danger")
        return redirect(url_for('index'))

    if file:
        # Save the uploaded file to the specified upload folder
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        
        try:
            # Make predictions based on the uploaded file
            predictions = predict_credit_scores(file_path)
            if predictions.empty:
                flash("No predictions could be made, check the input data.", "danger")
                return redirect(url_for('index'))
        except ValueError as e:
            flash(f"Input Error: {str(e)}", "danger")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error during prediction: {str(e)}", "danger")
            return redirect(url_for('index'))

        # Convert predictions DataFrame to HTML with customized styles
        predictions_html = predictions.to_html(classes='table table-striped', index=False)

        # Adding inline CSS to change the predicted credit score color to white
        predictions_html = predictions_html.replace(
            '<th>predicted_credit_score</th>',
            '<th style="color: white;">predicted_credit_score</th>'
        )
        predictions_html = predictions_html.replace(
            '<td>', '<td style="color: white;">'
        )

        # Change the color of specific headings to #ffd700
        headings_to_color = [
            'loan_amount', 'open_accounts', 'credit_history_length',
            'defaulted_before', 'education_level', 'employment_status',
            'savings', 'debt_to_income_ratio', 'credit_score'
        ]
        
        for heading in headings_to_color:
            predictions_html = predictions_html.replace(
                f'<th>{heading}</th>',
                f'<th style="color: #ffd700;">{heading}</th>'
            )

        os.remove(file_path)  # Cleanup the uploaded file
        
        # Render the index page with predictions
        return render_template('index.html', predictions=predictions_html)

@app.route('/wallet/add-transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Retrieve transaction data from the form
        date = request.form.get('date')
        description = request.form.get('description')
        amount = request.form.get('amount')
        transaction_type = request.form.get('type')

        # Input validation for transaction data
        if not date or not description or not amount or not transaction_type:
            flash("All fields are required", "danger")
            return redirect(url_for('add_transaction'))

        try:
            amount = float(amount)  # Ensure amount is a float
            if amount <= 0:
                flash("Amount must be greater than zero", "danger")
                return redirect(url_for('add_transaction'))
        except ValueError:
            flash("Amount must be a valid number", "danger")
            return redirect(url_for('add_transaction'))

        # Logic to save the transaction (to a database or a file) can go here
        # For demonstration, we will just print it out
        print(f"Transaction added: {date}, {description}, {amount}, {transaction_type}")
        
        flash("Transaction added successfully!", "success")
        return redirect(url_for('wallet'))  # Redirect to the wallet page

    return render_template('add_transaction.html')

@app.route('/wallet')
def wallet():
    # Render the wallet page
    return render_template('wallet.html')

if __name__ == '__main__':
    # Create the uploads folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        
    # Start the Flask application
    app.run(debug=True)
