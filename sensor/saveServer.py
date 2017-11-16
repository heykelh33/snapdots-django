# saved as save-server.py
import Pyro4
# Server Connection to MySQL:
import MySQLdb
from multiprocessing import Process
import sys
sys.path.insert(0, "../")
from snapdots.asgi   import channel_layer
from channels import Group
import json


class SaveServer(object):

    def __init__(self):
        proc = Process(target=self.damon, args=())
        proc.start()
       


    @Pyro4.expose
    def save(self,var,time, data):  
        type = 1
        if var == 'Humidity':
            type = 2
            print("Save server data: ",data)
            Group("sensor_humidity").send({'text': str(data)})
        else:
            print("Save server data: ",data)
            Group("sensor").send({'text': str(data)})

        conn = MySQLdb.connect(host="localhost",
                               user="root",
                               passwd="root",
                               db="sensordb")
        x = conn.cursor()
        try:
            x.execute("INSERT INTO data (type, date_time,value) values (%s,%s,%s)", (type, time, data))
            conn.commit()
        except Exception, e:
            print str(e)
            conn.rollback()
        conn.close()
            
    def damon(self):
        daemon = Pyro4.Daemon()  # make a Pyro daemon
        ns = Pyro4.locateNS()  # find the name server
        uri = daemon.register(self)  # register the save maker as a Pyro object
        ns.register("sensor.save", uri)  # register the object with a name in the name server
        print("Save-server Ready.")
        daemon.requestLoop()  # start the event loop of the server to wait for calls


