from flask import Flask, render_template, redirect, url_for, request
#import webtier
#import mysql.connector
#import socket

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET','POST'])
def home():
    error = None
    connected = None
    if request.method == 'POST':
        #if runWebSocket('1') == 'True':
            connected = 'Successfully connected to the database' #or redirect to home
            return render_template('home.html', connected=connected)
        #else:
            error = 'Could not connect to the database'
    return render_template('home.html', error=error)

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    username = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            username = request.form['username']
            #return render_template('login.html', username=username)
            return redirect(url_for('landing'))
        #username = request.form['username']
        #message = '2,' + username + ',' + request.form['password']
        #if runWebSocket(message) == 'True':
        #    return render_template('login.html', username=username)
        #else:
         #   error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)


@app.route("/landing")
def landing():
    return render_template('landing.html')


def runWebSocket(message):
    dao_sender_host = '172.17.128.1'
    dao_sender_port = 5000

    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((dao_sender_host, dao_sender_port))

        clientsocket.send(bytes(message, 'UTF-8'))
        buffer = clientsocket.recv(8000).decode('UTF-8')
        print(buffer)
        clientsocket.close()
        return buffer
    except Exception as e:
        print(e)
        print("Could not connect client socket DAO")
        return None


if __name__ == "__main__":
    app.run(debug=True)
    #webtier.bootapp()
