from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the AI model
model = joblib.load('credit_model.pkl')

# Function to preprocess the data and predict credit scores
def predict_credit_scores(file_path):
    data = pd.read_csv(file_path)
    features = ['age', 'income', 'loan_amount', 'open_accounts', 'credit_history_length', 
                'defaulted_before', 'education_level', 'employment_status', 'savings', 
                'debt_to_income_ratio']
    X = data[features]
    credit_scores = model.predict(X)
    data['predicted_credit_score'] = credit_scores
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part in request"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No file selected"
    
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        predictions = predict_credit_scores(file_path)
        predictions_html = predictions.to_html()  # Convert DataFrame to HTML for display
        
        return render_template('index.html', predictions=predictions_html)

@app.route('/wallet/add-transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Here you would handle the form submission for adding a transaction
        date = request.form['date']
        description = request.form['description']
        amount = request.form['amount']
        transaction_type = request.form['type']

        # Logic to save the transaction (to a database or a file) can go here
        
        # Redirect to the wallet page after adding a transaction
        return redirect(url_for('wallet'))  # Redirecting to the wallet route

    return render_template('add_transaction.html')

@app.route('/wallet')
def wallet():
    # Pass data to wallet.html as needed
    return render_template('wallet.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
