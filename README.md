🏥 Hospital System – Video Calling with Doctors

A complete Flask + MySQL telemedicine web application where patients can book appointments, make payments, start video consultations and chat in real-time with doctors.

👩‍💻 Developed By

Yusra Perween

🚀 Features
👤 Authentication

Patient & Doctor Registration

Secure Login / Logout

Role-based Dashboard

📅 Appointment System

Patients can book appointments

Doctors can view appointments

Cancel & Complete appointment feature

💳 Payment Gateway (Demo)

Fake payment page (Stripe removed)

Payment recorded in MySQL database

🎥 Video Consultation

Start video call after booking

Camera & microphone access

WebRTC based video consultation UI

💬 Live Chat During Video Call (NEW ⭐)

Real-time chat between patient and doctor

Built using Flask-SocketIO (WebSockets)

Messages appear instantly without refreshing page

🗄️ Database

MySQL database stores:

Users

Doctors

Appointments

Payments

🛠️ Tech Stack
Technology	Used
Python	Flask
Database	MySQL
Frontend	HTML, CSS, JavaScript
Real-time Chat	Flask-SocketIO
Video	WebRTC
📂 Project Structure
Hospital-System-Video-Calling-with-Doctors
│
├── static/
├── templates/
├── app.py
├── config.py
├── database.sql
├── requirements.txt
└── README.md
⚙️ How to Run This Project

🔹 1. Clone the Repository
git clone https://github.com/Yusra-Perween/Hospital-System-Video-Calling-with-Doctors.git
cd Hospital-System-Video-Calling-with-Doctors

🔹 2. Start XAMPP Services

Open XAMPP Control Panel and start:

Apache

MySQL

🔹 3. Create the Database

Open in browser:

http://localhost/phpmyadmin

Create database:

hospital_db

Import file:

database.sql

🔹 4. Configure Database Connection

Open config.py:

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DB = "hospital_db"
MYSQL_PORT = 3306

🔹 5. Install Required Libraries
pip install -r requirements.txt

🔹 6. Run the Application
python app.py

You will see:

Running on http://127.0.0.1:5000/

🔹 7. Open in Browser
http://127.0.0.1:5000
🎯 Future Improvements

AI Symptom Checker 🤖

Doctor recommendation system

Email notifications

Real payment gateway integration
