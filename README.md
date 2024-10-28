# SMME Financial Technology Inclusion (FTI) Portal

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-MVP-orange.svg)

## Description
This repository contains the code for the **SMME Financial Technology Inclusion (FTI) Portal**, a Minimum Viable Product (MVP) aimed at empowering small, medium, and micro enterprises (SMMEs) in underserved communities. This portal enhances access to essential financial services, educational resources, and market insights, supporting economic growth and digital inclusion.

## MVP Summary
The SMME Financial Technology Inclusion (FTI) Portal is designed to provide a scalable platform that supports financial access and educational growth for SMMEs. By integrating core functionalities such as digital wallets, user role management, and educational resources, this MVP serves as a vital tool for fostering economic empowerment and driving transformative impact within communities.

## Features
- **Admin Dashboard**: Access advanced settings, user management, and reporting tools.
- **User Digital Wallet**: Securely manage financial transactions and track balances with ease.
- **Guest Information Access**: Allows guest users to explore the platform's resources and understand its features.
- **Role-Based Access**: Users select their role (Admin, User, Guest) for customized access to platform features.
- **Educational Resources**: Comprehensive resources designed to increase financial literacy and promote informed decision-making.

## Comprehensive Flow
1. **User Role Selection**: Users select their role (Admin, User, or Guest) on the homepage for customized functionality.
2. **Dynamic Feature Display**:
   - **Admin**: Access to the Admin Dashboard, user management, and reporting tools.
   - **User**: Access to the Digital Wallet, allowing financial management and transaction tracking.
   - **Guest**: View informational resources without the need to sign up.
3. **Financial Access and Management**: Through the Digital Wallet, users can view and manage their financial transactions.
4. **Data Management**: Admins can monitor user activities, manage documents, and analyze data through built-in reporting tools.
5. **Educational Resources**: All users have access to financial literacy resources that cover various topics, from budgeting to investment.

## Technologies Used
This project integrates a range of technologies for both frontend and backend functionalities:
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap, Font Awesome
- **Backend**: Flask for API development and server-side logic
- **Data Handling and Machine Learning**: Pandas, Scikit-learn, Joblib, and Web3 for data processing and model deployment

## Installation & Setup
Follow these steps to set up and run the project on your local environment.

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Steps

#### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/Thando12345/SMME-FTI-Portal.git
cd SMME-FTI-Portal


### 2. Create a Virtual Environment
Set up a virtual environment to manage project dependencies. This isolates the dependencies of this project from others on your system.

```bash
python3 -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

### 3. Install Flask and Other Dependencies
Install Flask and other required packages. If a `requirements.txt` file is available, use it to install dependencies in bulk; otherwise, install each dependency individually.

**Using requirements.txt:**
```bash
pip install -r requirements.txt


### 4. Set Up Environment Variables
To securely configure the application, create a `.env` file in the project’s root directory. This file will store necessary environment variables.

**Sample .env Configuration:**
```makefile
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url


### 5. Run Migrations (If applicable)
If the project involves a database, set it up by running initial migrations:
```bash
flask db init
flask db migrate
flask db upgrade


### 6. Start the Application
Launch the Flask application. The application will be accessible at `http://127.0.0.1:5000`:
```bash
flask run

