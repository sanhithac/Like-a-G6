from DatabaseConnector import *
from DatabaseServerSocket import *


connection = connectDb()
checkConnection(connection)
basicQuery(connection)
checkLogin(connection, 'alison', 'gradprog2016@07')

#runServerSocketDao()

#run client socket and server socket from different terminals

