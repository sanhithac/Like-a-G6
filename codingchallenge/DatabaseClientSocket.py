import socket

def runClientSocketDao(message):
    dao_sender_host = '127.0.0.1'
    dao_sender_port = 8089

    message = '1'
    #this is temporary

    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((dao_sender_host, dao_sender_port))

        clientsocket.send(bytes(message, 'UTF-8'))
        buffer = clientsocket.recv(1024).decode('UTF-8')
        print(buffer)
        clientsocket.close()
        return buffer
    except Exception as e:
        print(e)
        print("Could not connect client socket DAO")
        return None



runClientSocketDao('temp')