from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from flask_mysqldb import MySQL
import pymysql
from flask_wtf import Form
from sympy.integrals.rubi.utility_function import First
from wtforms.fields import DateField
import os
import requests

app = Flask(__name__)
Bootstrap(app)
datepicker(app)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)
print("success")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/patientRegistration', methods=['GET', 'POST'])
def patientRegistration():
    return render_template('patient.html')


@app.route('/ptregistration', methods=['GET', 'POST'])
def ptregistration():
    if request.method == "POST":
        fname = request.form.get('first_name')
        lname = request.form.get('last_name')
        a = request.form.get('age')
        email = request.form.get('patient_email')
        print(fname, lname, a, email)
        cur = mysql.connection.cursor()
        sql = "INSERT INTO hospital (first_name,last_name, age,patient_email) VALUES (%s,%s,%s,%s)"
        val = (fname, lname, a, email)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('appoinment'))


@app.route('/appoinment', methods=['GET', 'POST'])
def appoinment():
    return render_template('appoinment.html')


@app.route('/pt_appt', methods=['GET', 'POST'])
def pt_appt():
    if request.method == "POST":
        id =request.form.get('id')
        patient_name = request.form.get('patient_name')
        gender = request.form.get('gender')
        SelectDate = request.form.get('SelectDate')
        appt = request.form.get('appt')
        Doctors_name = request.form.get('Doctors_name')
        Symptoms = request.form.get('Symptoms')
        print(id,patient_name, gender, SelectDate, appt, Doctors_name, Symptoms)
        cur = mysql.connection.cursor()
        sql = "INSERT INTO patient_appoinment (id,patient_name, gender, SelectDate, appt, Doctors_name, Symptoms)" \
              " VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (id,patient_name, gender, SelectDate, appt, Doctors_name, Symptoms)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))


@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    return render_template('doctor.html')


@app.route('/DoctorData', methods=['POST', 'GET'])
def DoctorData():
    if request.method == "POST":
        id=request.form.get('id')
        Name = request.form.get('Doctors_name')
        password = request.form.get('password')
        print(id,Name, password)
        cur = mysql.connection.cursor()
        sql = "INSERT INTO doctor_details (id,Doctors_name,password) VALUES (%s,%s,%s)"
        val = (id,Name, password)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
    return redirect('Doctors_view')


@app.route('/appt_view', methods=['POST', 'GET'])
def appt_view():
    return render_template('index')


@app.route('/up_appt')
def up_appt():
    if request.method == "POST":
        patient_name = request.form.get('patient_name')
        gender = request.form.get('gender')
        SelectDate=request.form.get('SelectDate')
        appt =request.form.get('appt')
        Symptoms=request.form.get('Symptoms')
        Doctors_name=request.form.get('Doctors_name')
        print(patient_name, gender, SelectDate, appt, Symptoms , Doctors_name)
        cur = mysql.connection.cursor()
        sql = "alter INTO patient_appoinment where (patient_name, gender, SelectDate, appt, Symptoms , Doctors_name) " \
              "VALUES (%s,%s,%s,%s,%s,%s) "
        val = (patient_name, gender, SelectDate, appt, Symptoms , Doctors_name)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
    return render_template('appoinment.html')


@app.route('/Doctors_view')
def Doctors_view():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient_appoinment")
    data = cur.fetchall()
    return render_template('DoctorData.html', data=data)


@app.route('/Pharmacy', methods=['POST', 'GET'])
def Pharmacy():
    return render_template('pharmacy.html')


@app.route('/Pharm_adata', methods=['POST', 'GET'])
def Pharm_adata():
    if request.method == "POST":
        id= request.form.get('id')
        MedicineName = request.form.get('MedicineName')
        Availability = request.form.get('Availability')
        Mfdate = request.form.get('Mfdate')
        Remaining = request.form.get('Remaining')
        Exdate = request.form.get('Exdate')
        NeedCount = request.form.get('NeedCount')
        print(id, MedicineName, Availability, Mfdate, Remaining, Exdate, NeedCount)
        cur = mysql.connection.cursor()
        sql = "INSERT INTO pharm_adata (id, MedicineName,Availability, Mfdate, Remaining, Exdate, NeedCount)" \
              " VALUES (%s,%s,%s,%s,%s,%s,%s) "
        val = (id,MedicineName, Availability, Mfdate, Remaining, Exdate, NeedCount)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
    return render_template('index.html')


@app.route('/Admin_login', methods=['POST', 'GET'])
def Admin_login():

    return render_template('Admin_login.html')


@app.route('/Admin', methods=['POST', 'GET'])
def Admin():
    return render_template('Admin.html')


@app.route('/dc_login')
def dc_login():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doctor_details")
    data = cur.fetchall()
    return render_template('dc_login.html', data=data)


@app.route('/ad_login', methods=['POST', 'GET'])
def ad_login():
    return render_template('index.html')


@app.route('/ad_dc', methods=['POST', 'GET'])
def ad_dc():
    if request.method == "POST":
        Name = request.form.get('Doctors_name')
        password = request.form.get('password')
        print(Name, password)
        cur = mysql.connection.cursor()
        sql = "INSERT INTO doctor_details (Doctors_name,password) VALUES (%s,%s)"
        val = (Name, password)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
    return redirect('doctor')


@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("delete from doctor_details where id =%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/Admin')


@app.route('/delete_pharm/<string:id>', methods=['POST', 'GET'])
def delete_pharm(id):
    cur = mysql.connection.cursor()
    cur.execute("delete from pharm_adata where id =%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/')


@app.route('/delete_appt/<string:id>', methods=['POST', 'GET'])
def delete_appt(id):
    cur = mysql.connection.cursor()
    cur.execute("delete from patient_appoinment where id =%s", (id,))
    mysql.connection.commit()
    return redirect('/')


@app.route('/dlt_pt', methods=['POST', 'GET'])
def dlt_pt():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient_appoinment")
    data = cur.fetchall()
    return render_template('dlt_pt.html', data=data)


@app.route('/ph_login', methods=['POST', 'GET'])
def ph_login():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pharm_adata")
    data = cur.fetchall()
    return render_template('ph_login.html', data=data)


@app.route('/Delete_doctor <string:Doctors_name>', methods=['POST', 'GET'])
def delete_doctor(Delete_doctor):
        Doctors_name = request.form.get('Doctors_name')
        print(Doctors_name)
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM doctor_details WHERE Doctors_name = %s", (Doctors_name,))
        print("success")
        return render_template('Delete_doctor.html')


@app.route('/Update_Pharma')
def Update_Pharma():
    if request.method == "POST":
        MedicineName = request.form.get('MedicineName')
        Availability = request.form.get('Availability')
        Mfdate=request.form.get('Mfdate')
        Remaining =request.form.get('Remaining')
        Exdate=request.form.get('Exdate')
        NeedCount=request.form.get('NeedCount')
        print(MedicineName, Availability, Mfdate, Remaining, Exdate , NeedCount)
        cur = mysql.connection.cursor()
        sql = "alter INTO pharm_adata where (MedicineName, Availability, Mfdate, Remaining, Exdate , NeedCount) " \
              "VALUES (%s,%s,%s,%s,%s,%s) "
        val = (MedicineName, Availability, Mfdate, Remaining, Exdate , NeedCount)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
    return render_template('Pharmacy.html')


if __name__ == '__main__':
    app.run(debug=True)
