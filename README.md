# ReWheel Repository

**ReWheel** is an automotive parts tracking web application built with Flask, SQLAlchemy, WTForms, and Bootstrap. Developed as part of the E-Business & Digitale Geschäftsmodelle course at HWR Berlin, this repository contains the full codebase and documentation with GitHub Pages.

## ReWheel Contents

The website is a Flask-powered platform where users can register either as customers or suppliers. Customers browse and search for automotive parts in the catalogue, add items to their cart, and place orders by providing shipping details and confirming payment. Suppliers can log in to list new parts with details such as name, price, availability, and images; they can also manage their listings and confirm shipping once payment is received. The site tracks each user’s orders and provides a simple checkout flow using an advance bank transfer. The interface includes a main catalogue page, login, registration, cart, and profile settings, ensuring both roles can interact efficiently with the system.

## Steps to Execute the App

### Step 1: Set up a Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows use 'venv\Scripts\activate'
```

### Step 2: Install Requirements

Install the necessary Python packages with:

```bash
pip install -r requirements.txt
```

### Step 3: Start the Development Server

Run the server using:

```bash
python app.py
```

**Expected output:**

```plaintext
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Step 4: Access the Application

Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the main page and start using ReWheel after registering and logging in.

## Features

- **User Authentication**: Secure login and registration, with separate roles for "customer" and "supplier".
- **Part Offering**: Suppliers can add new automotive parts with details like price, quantity, and estimated delivery.
- **Catalogue**: Customers can browse available parts and view detailed information if logged in.
- **Buying and Selling**: Facilitates transactions through ReWheel’s marketplace.
- **Eco Badge**: Show users that a supplier is
working environmental friendly.
