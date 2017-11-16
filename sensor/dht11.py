__author__ = 'guille'

import Pyro4
from sensorABC import Sensor

from requestData import RequestData
from dataJson import DataJson

class Dht11(Sensor):

    def __init__(self,id, variable, type, gpiopin,arduDriver):
		    super(Dht11, self).__init__(id, variable, type, gpiopin,arduDriver)


    def read(self,idContainer,time):
        requestData = RequestData(idContainer,self.id,'<H',time)
        requestDataJson = requestData.asJson()
        print "sensor."+self.arduDriver+".enqueue"
        sensor_enqueue = Pyro4.Proxy("PYRONAME:sensor."+self.arduDriver+".enqueue")  # use name server object lookup uri shortcut
        sensor_enqueue.enqueue(requestDataJson)

    #Este metodo se debe mejorar hablar con ramon
    def recive(self,sensorData):        
        print "dht11humidity data: "
	    # print sensorData.getVariable()
        print sensorData.getVariable()[0]=='H'
        humidity_dht11 = -1
        if sensorData.getVariable()[0] == 'H':
	        # print sensorsorData.getValue()[0]
            humidity_dht11 = float(sensorData.getValue()[0])
            save_server = Pyro4.Proxy("PYRONAME:sensor.save")  # use name server object lookup uri shortcut
            print sensorData.getTime()
            save_server.save("Humidity", sensorData.getTime(), humidity_dht11)

