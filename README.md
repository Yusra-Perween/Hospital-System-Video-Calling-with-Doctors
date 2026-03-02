# 🏥 Hospital System – Video Calling with Doctors

A complete **Flask + MySQL web application** where patients can book appointments, make payments and do video consultation with doctors.

---

## 👩‍💻 Developed By
**Yusra Perween**

---

## 🚀 Features

### 👤 Authentication
- Patient & Doctor Registration
- Login / Logout system
- Role based dashboard

### 📅 Appointment System
- Patients can book appointments
- Doctors can view appointments
- Cancel & Complete appointment feature

### 💳 Payment Gateway (Demo)
- Fake payment page (Stripe removed)
- Payment recorded in database

### 🎥 Video Consultation
- Start video call after booking
- Camera + microphone access
- Real-time consultation UI

### 🗄️ Database
- MySQL database integration
- Stores users, doctors, appointments & payments

---

## 🛠️ Tech Stack

| Technology | Used |
|------------|------|
| Python | Flask |
| Database | MySQL |
| Frontend | HTML, CSS, JS |
| Backend | Flask |
| Video | WebRTC |

---

## 📂 Project Structure
Hospital-System-Video-Calling-with-Doctors
│
├── static/
├── templates/
├── app.py
├── config.py
├── database.sql
├── requirements.txt
└── README.md

---

## ⚙️ How to Run This Project

🔹 1. Clone the Repository
git clone https://github.com/Yusra-Perween/Hospital-System-Video-Calling-with-Doctors.git
cd Hospital-System-Video-Calling-with-Doctors

🔹 2. Start XAMPP Services

Open XAMPP Control Panel and start:

Apache

MySQL

Keep XAMPP running in the background.

🔹 3. Create the Database

Open browser and go to:

http://localhost/phpmyadmin

Click New and create database:

hospital_db

Select the database → Click Import

Import the file:

database.sql

🔹 4. Configure Database Connection

Open config.py and ensure MySQL credentials match your XAMPP setup:

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DB = "hospital_db"
MYSQL_PORT = 3306

🔹 5. Install Required Libraries

Open terminal inside the project folder and run:

pip install -r requirements.txt

🔹 6. Run the Application

Start the Flask server:

python app.py

You should see:

Running on http://127.0.0.1:5000/

🔹 7. Open in Browser

Visit the application in your browser:

http://127.0.0.1:5000
