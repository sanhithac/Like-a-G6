import json
import MySQLdb as m
import codingchallenge.Queries as q

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


def checkConnection1(connection):
    if connection:
        print("Connected to database")
        return True
    else:
        print("Could not connect to database")
        return False


def basicQuery(connection):
    if checkConnection1(connection):
        cursor = connection.cursor()
        try:
            cursor.execute(q.query_test)
        except m.Error as e:
            print(e)
            return False

        result = cursor.fetchall()
        print(result)

        json_list = convertTupleToJson(result)
        print(json_list)
        print(type(json_list))

        return True

    else:
        return False


def checkLogin2(connection, user, password):

    if checkConnection1(connection):
        cursor = connection.cursor()
        try:
            cursor.execute(q.query2, (user, password))
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


# UPDATE 7
def avgPriceQuery7(connection):
    if checkConnection1(connection):
        cursor = connection.cursor()
        try:
            cursor.execute(q.query7)
        except m.Error as e:
            print(e)
            return 'False'

        result = cursor.fetchall()
        json_list = convertTupleToJson(result)

        return json_list

    else:
        return 'False'


# UPDATE 8
def endingPositionQuery8(connection):
    if checkConnection1(connection):
        cursor = connection.cursor()
        try:
            cursor.execute(q.query8)
        except m.Error as e:
            print(e)
            return 'False'

        result = cursor.fetchall()
        json_list = convertTupleToJson(result)

        return json_list

    else:
        return 'False'


# UPDATE 9
def realizedPL9(connection):
    if checkConnection1(connection):
        cursor = connection.cursor()
        try:
            cursor.execute(q.query9)
        except m.Error as e:
            print(e)
            return 'False'

        result = cursor.fetchall()
        json_list = convertTupleToJson(result)

        return json_list

    else:
        return 'False'


# UPDATE 10
def effectivePL10(connection):
    if checkConnection1(connection):
        cursor = connection.cursor()
        try:
            cursor.execute(q.query10)
        except m.Error as e:
            print(e)
            return 'False'

        result = cursor.fetchall()
        json_list = convertTupleToJson(result)

        return json_list

    else:
        return 'False'


def convertTupleToJson(result):
    list_result = []
    for row in result:
        fin_row = list(row)
        fin_row = [str(x) for x in fin_row]
        list_result.append(fin_row)

    json_list = json.dumps(list_result)
    return json_list
