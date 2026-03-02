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

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Yusra-Perween/Hospital-System-Video-Calling-with-Doctors.git
cd Hospital-System-Video-Calling-with-Doctors
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Setup MySQL Database

Open phpMyAdmin and run:

database.sql
4️⃣ Update config.py

Set your MySQL username & password.

5️⃣ Run the project
python app.py

Open in browser:

http://127.0.0.1:5000
🎯 Future Improvements

Real Stripe payment integration

Online doctor approval system

Chat system

Email notifications
