# ATM Management System

## 📌 Project Overview

The **ATM Management System** is a web-based application that simulates basic ATM operations such as user registration, login, balance checking, deposit, and withdrawal. The system provides a simple interface where users can manage their account transactions securely.

This project is built using **Python**, **Flask**, **SQLite**, **HTML**, and **CSS**.

---

## 🚀 Features

* User Registration
* User Login Authentication
* Check Account Balance
* Deposit Money
* Withdraw Money
* Dashboard Interface
* Navigation Menu for ATM Operations

---

## 🛠️ Technologies Used

* **Python**
* **Flask (Web Framework)**
* **SQLite Database**
* **HTML5**
* **CSS3**

---

## 📂 Project Structure

```
ATM/
│
├── app.py                # Main Flask application
├── add_user.py           # Script to add users
├── db_setup.py           # Database setup script
├── atm.db                # SQLite database
│
├── static/
│   └── style.css         # Styling for the application
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── deposit.html
│   ├── withdraw.html
│   ├── balance.html
│   ├── navbar.html
│   └── side_navbar.html
│
└── venv/                 # Virtual environment (not required to upload)
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/makhila-2005/ATM.git
```

### 2. Navigate to the project directory

```
cd ATM
```

### 3. Create a virtual environment

```
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```
venv\Scripts\activate
```

### 5. Install required dependencies

```
pip install flask
```

### 6. Setup the database

```
python db_setup.py
```

### 7. Run the application

```
python app.py
```

### 8. Open in browser

```
http://127.0.0.1:5000
```

---

## 📊 Functional Modules

### User Authentication

Users can register and log in to access ATM functionalities.

### Account Operations

* Deposit money into account
* Withdraw money from account
* Check current account balance

### Dashboard

Provides a simple navigation interface to access ATM operations.

---

## 🔒 Future Improvements

* PIN-based authentication
* Transaction history
* Admin panel for user management
* Enhanced security features
* Responsive UI design

---

## 👩‍💻 Author

**Akhila Mulukutla**

---

## 📜 License

This project is for educational purposes.
