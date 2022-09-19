from flask import Flask, session, render_template, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = "secret_key"
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='oberon'
app.config['MYSQL_PASSWORD']='Welcome2021!'
app.config['MYSQL_DB']='task_app'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    msg=''
    return render_template('login.html', msg='')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)