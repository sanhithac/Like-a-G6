import codingchallenge.DatabaseConnector as dc
import codingchallenge.DatabaseServerSocket as dss
import threading
from time import sleep

from codingchallenge.consume_stream import dealData

#connection = dc.connectDb()
#dc.checkConnection1(connection)
#dc.basicQuery(connection)
#dc.checkLogin2(connection, 'alison', 'gradprog2016@07')

#dc.avgPriceQuery7(connection)
#dc.endingPositionQuery8(connection)
#dc.effectivePL10(connection)

#dss.runServerSocketDao()

#run client socket and server socket from different terminals


class Threads:
    def __init__(self):
        self.lock = threading.Lock()
        self.deal = None

    def insertNewDeals(self):
        dealData()

    def runServer(self):
        dss.runServerSocketDao()

    def go(self):
        th1 = threading.Thread(target=self.insertNewDeals)
        th2 = threading.Thread(target=self.runServer)
        th1.start()
        th2.start()


t = Threads()
t.go()

