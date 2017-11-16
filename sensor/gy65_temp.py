__author__ = 'root'

import Pyro4
from sensorABC import Sensor

from requestData import RequestData
from dataJson import DataJson

class Gy65_temp(Sensor):
    def __init__(self, id, variable, type, gpiopin,arduDriver):
        super(Gy65_temp, self).__init__(id, variable, type, gpiopin,arduDriver)


    def read(self,idContainer,time):
        requestData = RequestData(idContainer,self.id,'<T',time)
        requestDataJson = requestData.asJson()
        print "sensor."+self.arduDriver+".enqueue"
        sensor_enqueue = Pyro4.Proxy("PYRONAME:sensor."+self.arduDriver+".enqueue")  # use name server object lookup uri shortcut
        sensor_enqueue.enqueue(requestDataJson)

    #Este metodo se debe mejorar hablar con ramon
    def recive(self,sensorData):        
        print "gy65temp data: "
	    # print sensorData.getVariable()
        print sensorData.getVariable()[0]=='T'
        temperatura_ds18b20 = -1
        if sensorData.getVariable()[0] == 'T':
	        # print sensorsorData.getValue()[0]
            temperatura_ds18b20 = float(sensorData.getValue()[0]) / 10
            save_server = Pyro4.Proxy("PYRONAME:sensor.save")  # use name server object lookup uri shortcut
            print sensorData.getTime()
            save_server.save("Temperature", sensorData.getTime(), temperatura_ds18b20)


#Gy65_temp("Gy65_temp","Temperatura", "1", 1,"ardu1")
