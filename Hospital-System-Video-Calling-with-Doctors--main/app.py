from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_mysqldb import MySQL
import config

import time
import secrets


app = Flask(__name__)
app.secret_key = "my_super_secret_key_123"

# MySQL configuration from config.py
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
app.config['MYSQL_PORT'] = config.MYSQL_PORT
mysql = MySQL(app)


# homepage
@app.route('/')
def index():
    return render_template('index.html')


# user registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
                    (name, email, password, role))

        if role == 'doctor':
            user_id = cur.lastrowid
            cur.execute("INSERT INTO doctors (user_id, specialization, bio) VALUES (%s, %s, %s)",
                        (user_id, request.form['specialization'], request.form['bio']))

        mysql.connection.commit()
        cur.close()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


# user login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()

        if user:
            session['user_id'] = user[0]
            session['role'] = user[4]
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'danger')
    return render_template('login.html')

# user dashboard page
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    if session['role'] == 'patient':
        cur.execute("""
            SELECT a.id, a.patient_id, u.name as doctor_name, 
                a.appointment_date, a.appointment_time, a.status
            FROM appointments a
            JOIN doctors d ON a.doctor_id = d.id
            JOIN users u ON d.user_id = u.id
            WHERE a.patient_id = %s
            ORDER BY a.appointment_date, a.appointment_time
        """, (session['user_id'],))
    elif session['role'] == 'doctor':
        cur.execute("""
        SELECT a.id, a.doctor_id, u.name as patient_name,
            a.appointment_date, a.appointment_time, a.status
        FROM appointments a
        JOIN users u ON a.patient_id = u.id
        JOIN doctors d ON a.doctor_id = d.id
        WHERE d.user_id = %s
        ORDER BY a.appointment_date, a.appointment_time
    """, (session['user_id'],))
    appointments = cur.fetchall()
    cur.close()
    return render_template('dashboard.html', appointments=appointments)

# User appointment booking route
@app.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    if 'user_id' not in session or session['role'] != 'patient':
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doctors WHERE approval_status = 'approved'")
    doctors = cur.fetchall()

    if request.method == 'POST':
        # Store appointment data in session BEFORE payment
        session['temp_appointment'] = {
            'doctor_id': request.form['doctor_id'],
            'appointment_date': request.form['date'],
            'appointment_time': request.form['time']
        }

        return redirect(url_for('payment_page'))   # ← must be INSIDE POST

    return render_template('book_appointment.html', doctors=doctors)

# Fake payment page (no Stripe)
@app.route('/payment')
def payment_page():
    if 'temp_appointment' not in session:
        return redirect(url_for('book_appointment'))
    return render_template('payment.html')

# payment route
@app.route('/payment_success')
def payment_success():
    if 'temp_appointment' not in session:
        flash('Session expired', 'danger')
        return redirect(url_for('book_appointment'))

    temp_data = session.pop('temp_appointment')
    cur = mysql.connection.cursor()

    # Insert appointment
    cur.execute("""
        INSERT INTO appointments
        (patient_id, doctor_id, appointment_date, appointment_time, status)
        VALUES (%s, %s, %s, %s, 'booked')
    """, (session['user_id'], temp_data['doctor_id'],
          temp_data['appointment_date'], temp_data['appointment_time']))

    appointment_id = cur.lastrowid

    # Fake payment record
    cur.execute("""
        INSERT INTO Payments (appointment_id, stripe_payment_id, amount, status)
        VALUES (%s, %s, %s, 'completed')
    """, (appointment_id, "FAKE_PAYMENT", 2000))

    mysql.connection.commit()
    cur.close()

    flash('Appointment booked successfully!', 'success')
    return redirect(url_for('dashboard'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


# Cancel Appointment
@app.route('/cancel/<int:appointment_id>')
def cancel_appointment(appointment_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("UPDATE appointments SET status = 'cancelled' WHERE id = %s", (appointment_id,))
    mysql.connection.commit()
    cur.close()
    flash('appointment cancelled!', 'success')
    return redirect(url_for('dashboard'))





@app.route('/complete/<int:appointment_id>')
def complete_appointment(appointment_id):
    if 'user_id' not in session:
        return redirect('/login')

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE appointments SET status = 'completed' WHERE id = %s", (appointment_id,))
    mysql.connection.commit()
    cursor.close()

    return redirect('/dashboard')

# Video consultation page
@app.route('/video_consultation/<int:appointment_id>')
def video_consultation(appointment_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT a.id, u.name
        FROM appointments a
        JOIN users u ON u.id = a.patient_id
        WHERE a.id = %s
    """, (appointment_id,))
    appointment = cur.fetchone()
    cur.close()

    if not appointment:
        flash("Appointment not found", "danger")
        return redirect(url_for('dashboard'))

    return render_template('video_call.html', appointment_id=appointment_id)

if __name__ == '__main__':
    app.run(debug=True)

