import socket

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
            # result = handleData(buffer)
            connection.send(bytes('hello from server', 'UTF-8'))

    except Exception as e:
        print(e)
        print("Could not connect server socket DAO")
        return