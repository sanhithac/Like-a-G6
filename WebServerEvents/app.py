from flask import Flask, render_template, redirect, url_for, request
import webtier
import mysql.connector
import socket

app = Flask(__name__, template_folder='templates')

#mysql.connector.connect(host='127.0.0.1', database='mysql-server', user='root', password='ppp')


@app.route('/', methods=['GET','POST'])
def home():
    error = None
    connected = None
    if request.method == 'POST':
        if runWebSocket('1') is 'true':
            connected = 'Successfully connected to the database' #or redirect to home
            return render_template('home.html', connected=connected)
        else
            error = 'Could not connect to the database'
    return render_template('home.html', error=error)

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    username = None
    if request.method == 'POST':
        #if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        #    error = 'Invalid Credentials. Please try again.'
        #else:
        #    username = request.form['username']
            #return render_template('login.html', username=username)
        #    return redirect(url_for('landing'))
        username = request.form['username']
        message = username + ',' + request.form['password'] + ',2'
        if runWebSocket(message) is 'true'
            return render_template('login.html', username=username)
        else
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)


@app.route("/landing")
def landing():
    return "hi"


def runWebSocket(message):
    host = "127.0.0.1"
    port = 5000
    websocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    websocket.connect((host, port))
    websocket.send(message.encode())
    response = ''
    response = websocket.recv(1024).decode()
    return response


if __name__ == "__main__":
    runWebSocket()
    app.run(debug=True)
    #webtier.bootapp()
