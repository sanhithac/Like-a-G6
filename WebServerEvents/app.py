

from flask import Flask, render_template, redirect, url_for, request
#import webtier
import socket

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    connected = None
    if request.method == 'POST':
        if runWebSocket('1') == 'True':
            connected = 'Successfully connected to the database'  # or redirect to home
            return render_template('home.html', connected=connected)
        else:
            error = 'Could not connect to the database'
    return render_template('home.html', error=error)


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    username = None
    if request.method == 'POST':
        # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        #    error = 'Invalid Credentials. Please try again.'
        # else:
        #    username = request.form['username']
        # return render_template('login.html', username=username)
        #    return redirect(url_for('landing'))
        username = request.form['username']
        message = '2,' + username + ',' + request.form['password']
        if runWebSocket(message) == 'True':
            return render_template('login.html', username=username)
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)


@app.route("/landing", methods=['GET', 'POST'])
def landing():
    error = None
    if request.method == 'POST':
        if request.form['Connect'] == 'See Avg Buy and Sell':
           return redirect(url_for('avg'))
        elif request.form['Connect'] == 'See Ending Positions':
            return redirect(url_for('ending'))
        elif request.form['Connect'] == 'See Realized Profit and Loss':
            return redirect(url_for('avg'))
        elif request.form['Connect'] == 'See Effective Profit and Loss':
            return redirect(url_for('effective'))
        else:
            error = 'Something Went Wrong'
    return render_template('landing.html', error=error)


@app.route('/avg')
def avg():
    error = None
    info = runWebSocket('7')
    if info != 'False':
        return render_template('avg.html', info=info)
    else:
        error = 'Something Went Wrong, Select something else.'
        return render_template('avg.html', error=error)
    
    
@app.route('/ending')
def ending():
    error = None
    info = runWebSocket('8')
    if info != 'False':
        return render_template('ending.html', info=info)
    else:
        error = 'Something Went Wrong, Select something else.'
        return render_template('ending.html', error=error)


@app.route('/effective')
def effective():
    error = None
    info = runWebSocket('10')
    if info != 'False':
        return render_template('effective.html', info=info)
    else:
        error = 'Something Went Wrong, Select something else.'
        return render_template('effective.html', error=error)
    
    
def runWebSocket(message):
    dao_sender_host = '127.0.0.1'
    dao_sender_port = 8089

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
    # webtier.bootapp()

