import codingchallenge.DatabaseConnector as dc
import codingchallenge.DatabaseServerSocket as dss


connection = dc.connectDb()
#dc.checkConnection1(connection)
#dc.basicQuery(connection)
#dc.checkLogin2(connection, 'alison', 'gradprog2016@07')

#dc.avgPriceQuery7(connection)
#dc.endingPositionQuery8(connection)
#dc.effectivePL10(connection)

dss.runServerSocketDao()

#run client socket and server socket from different terminals

