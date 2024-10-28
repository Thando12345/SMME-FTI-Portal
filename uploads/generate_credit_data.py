import pandas as pd

# Define the data with 'credit_score' included
data = [
    {"age": 25, "income": 50000, "loan_amount": 2000, "open_accounts": 3, "credit_history_length": 5, "defaulted_before": 0, "education_level": "Bachelor", "employment_status": "Employed", "savings": 10000, "debt_to_income_ratio": 0.2, "credit_score": 650},
    {"age": 40, "income": 120000, "loan_amount": 5000, "open_accounts": 8, "credit_history_length": 15, "defaulted_before": 1, "education_level": "Master", "employment_status": "Self-employed", "savings": 20000, "debt_to_income_ratio": 0.3, "credit_score": 720},
    {"age": 35, "income": 75000, "loan_amount": 3000, "open_accounts": 4, "credit_history_length": 10, "defaulted_before": 0, "education_level": "Bachelor", "employment_status": "Unemployed", "savings": 5000, "debt_to_income_ratio": 0.5, "credit_score": 600},
    {"age": 50, "income": 95000, "loan_amount": 10000, "open_accounts": 6, "credit_history_length": 20, "defaulted_before": 0, "education_level": "PhD", "employment_status": "Employed", "savings": 15000, "debt_to_income_ratio": 0.25, "credit_score": 780},
    {"age": 29, "income": 65000, "loan_amount": 2500, "open_accounts": 5, "credit_history_length": 6, "defaulted_before": 0, "education_level": "High School", "employment_status": "Employed", "savings": 8000, "debt_to_income_ratio": 0.4, "credit_score": 640},
    {"age": 32, "income": 85000, "loan_amount": 4500, "open_accounts": 7, "credit_history_length": 12, "defaulted_before": 0, "education_level": "Master", "employment_status": "Employed", "savings": 12000, "debt_to_income_ratio": 0.35, "credit_score": 710},
    {"age": 45, "income": 100000, "loan_amount": 6000, "open_accounts": 9, "credit_history_length": 18, "defaulted_before": 1, "education_level": "Bachelor", "employment_status": "Self-employed", "savings": 25000, "debt_to_income_ratio": 0.28, "credit_score": 690},
    {"age": 28, "income": 70000, "loan_amount": 2800, "open_accounts": 4, "credit_history_length": 8, "defaulted_before": 0, "education_level": "PhD", "employment_status": "Employed", "savings": 6000, "debt_to_income_ratio": 0.3, "credit_score": 650},
    {"age": 38, "income": 110000, "loan_amount": 7500, "open_accounts": 5, "credit_history_length": 14, "defaulted_before": 0, "education_level": "Master", "employment_status": "Employed", "savings": 18000, "debt_to_income_ratio": 0.22, "credit_score": 740},
    {"age": 55, "income": 105000, "loan_amount": 9000, "open_accounts": 7, "credit_history_length": 22, "defaulted_before": 1, "education_level": "Bachelor", "employment_status": "Retired", "savings": 13000, "debt_to_income_ratio": 0.4, "credit_score": 630},
    {"age": 48, "income": 80000, "loan_amount": 3500, "open_accounts": 5, "credit_history_length": 16, "defaulted_before": 0, "education_level": "High School", "employment_status": "Self-employed", "savings": 2000, "debt_to_income_ratio": 0.45, "credit_score": 580},
    {"age": 31, "income": 67000, "loan_amount": 2200, "open_accounts": 4, "credit_history_length": 7, "defaulted_before": 0, "education_level": "Bachelor", "employment_status": "Employed", "savings": 7500, "debt_to_income_ratio": 0.37, "credit_score": 670},
    {"age": 42, "income": 95000, "loan_amount": 5000, "open_accounts": 6, "credit_history_length": 19, "defaulted_before": 0, "education_level": "Master", "employment_status": "Self-employed", "savings": 17000, "debt_to_income_ratio": 0.3, "credit_score": 730},
    {"age": 30, "income": 68000, "loan_amount": 2600, "open_accounts": 3, "credit_history_length": 9, "defaulted_before": 0, "education_level": "PhD", "employment_status": "Unemployed", "savings": 3000, "debt_to_income_ratio": 0.4, "credit_score": 640},
    {"age": 46, "income": 89000, "loan_amount": 4000, "open_accounts": 5, "credit_history_length": 15, "defaulted_before": 1, "education_level": "Master", "employment_status": "Employed", "savings": 16000, "debt_to_income_ratio": 0.33, "credit_score": 700},
    {"age": 37, "income": 76000, "loan_amount": 3200, "open_accounts": 4, "credit_history_length": 11, "defaulted_before": 0, "education_level": "Bachelor", "employment_status": "Employed", "savings": 11000, "debt_to_income_ratio": 0.27, "credit_score": 660},
    {"age": 40, "income": 88000, "loan_amount": 2900, "open_accounts": 5, "credit_history_length": 13, "defaulted_before": 0, "education_level": "High School", "employment_status": "Self-employed", "savings": 4000, "debt_to_income_ratio": 0.35, "credit_score": 670},
    {"age": 50, "income": 93000, "loan_amount": 5000, "open_accounts": 7, "credit_history_length": 20, "defaulted_before": 0, "education_level": "PhD", "employment_status": "Employed", "savings": 20000, "debt_to_income_ratio": 0.2, "credit_score": 750},
    {"age": 34, "income": 78000, "loan_amount": 3400, "open_accounts": 6, "credit_history_length": 12, "defaulted_before": 0, "education_level": "Master", "employment_status": "Employed", "savings": 10000, "debt_to_income_ratio": 0.32, "credit_score": 710},
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('credit_data.csv', index=False)

print("Data with 'credit_score' saved to credit_data.csv")
