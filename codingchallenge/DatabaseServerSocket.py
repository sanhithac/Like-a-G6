import socket
import codingchallenge.DatabaseConnector as dc


def runServerSocketDao():
    dao_listener_host = '127.0.0.1'
    dao_listener_port = 8089

    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((dao_listener_host, dao_listener_port))
        serversocket.listen(2) # become a server socket, maximum 5 connections
        print("server socket DAO is running")
        while True:
            connection, address = serversocket.accept()
            buffer = connection.recv(1024).decode('UTF-8')
            print(buffer)
            result = handleData(buffer)
            connection.send(bytes(result, 'UTF-8'))

    except Exception as e:
        print(e)
        print("Could not connect server socket DAO")
        return

def handleData(buffer):
    input = buffer.split(",")
    connection = dc.connectDb()

    if len(input) == 0 or len(input[0]) == 0:
        print('no input')
        return 'False'

    elif input[0] == '1' and len(input) == 1:
        result = str(dc.checkConnection1(connection))
        return result

    elif input[0] == '2' and len(input) == 3:
        result = str(dc.checkLogin2(connection, input[1], input[2]))
        return result

    elif input[0] == '7' and len(input) == 1:
        result = dc.avgPriceQuery7(connection)
        return result

    elif input[0] == '8' and len(input) == 1:
        result = dc.endingPositionQuery8(connection)
        return result

    elif input[0] == '9' and len(input) == 1:
        result = dc.realizedPL9(connection)
        return result

    elif input[0] == '10' and len(input) == 1:
        result = dc.effectivePL10(connection)
        return result

    else:
        print('could not identify')
        return 'False'
