from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from forms import RegistrationForm, LoginForm
import pymysql
import mysql.connector
import pandas as pd
import os
from audio_wave import *

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="emotion_recognition")
cursor = mydb.cursor()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(APP_ROOT, 'static/image/')
app.config['SECRET_KEY'] = 'b0b4fbefdc48be27a6123605f02b6b86'


def initialize():
    session['loggedin'] = False


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/application')
def application():
    return render_template('application.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return render_template('contact.html', message ="Message send successfully! We will contact you very soon!")
    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        email = request.form['email']

        password1 = request.form['pwd']

        sql = "select * from register where email='%s' and pwd='%s' " % (
            email, password1)
        print('q')
        x = cursor.execute(sql)
        print(x)
        results = cursor.fetchall()

        if len(results) > 0:
            name = results[0][1]
            flash("Welcome to website", "primary")
            return render_template('application.html', m="Login Success", msg=results[0][1])

        else:
            flash("Login failed", "warning")
            return render_template('login.html', msg="Login Failure!!!")
    return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['pwd']
        cpwd = request.form['cpwd']

        sql = "select * from register"
        result = pd.read_sql_query(sql, mydb)
        email1 = result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed", "warning")
            return render_template('register.html', msg="email existed")
        if (pwd == cpwd):
            sql = "INSERT INTO register (name,email,pwd,cpwd) VALUES (%s,%s,%s,%s)"
            val = (name, email, pwd, cpwd)
            cursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered", "warning")
            return render_template('login.html')
        else:
            flash("Password and Confirm Password not same", '')
        return render_template('register.html')

    return render_template('register.html')


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/audio/')

    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files["myaudio"]
    filename = file.filename
    if filename == "":
        flash('No File Selected', 'danger')
        return redirect(url_for('application'))

    destination = "/".join([target, filename])
    # Extension check
    ext = os.path.splitext(destination)[1]
    if (ext == ".wav"):
        pass
    else:
        flash("Invalid Extenstions! Please select a .wav audio file only.",
              category="danger")
        return redirect(url_for('application'))

    if not os.path.isfile(destination):
        file.save(destination)

    result = record_audio(record=False, file_loc=destination)
    new_dest = ('static/audio/'+str(filename))

    return render_template("upload.html", img_name=filename, emo=result, destination=new_dest)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    # flash('Logged Out Sucessfully!','success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
