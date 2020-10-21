import MySQLdb as m

def connectDb():
    try:
        connection = m.connect(host='localhost',
                                user='root',
                                db='db_grad_cs_1917',
                                passwd='ppp')
        return connection
    except m.Error as e:
        print(e)
        return False


def checkConnection(connection):
    if connection:
        print("Connected to database")
        return True
    else:
        print("Could not connect to database")
        return False


def basicQuery(connection):
    if checkConnection(connection):
        cursor = connection.cursor()
        try:
            cursor.execute("""SELECT * FROM deal LIMIT 10""")
        except m.Error as e:
            print(e)
            return False

        result = cursor.fetchall()
        for row in result:
            print(row)
        return True

    else:
        return False


def checkLogin(connection, user, password):
    if checkConnection(connection):
        cursor = connection.cursor()
        try:
            cursor.execute("""SELECT * FROM users WHERE user_id = %s AND 
                            user_pwd = %s""", (user, password))
        except m.Error as e:
            print(e)
            return False

        result = cursor.fetchall()

        if len(result) == 0:
            print("Log-in Doesn't Exist")
            return False

        else:
            print("Log-in Exists")
            return True

    else:
        return False