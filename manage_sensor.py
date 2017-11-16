__author__ = 'cyberguille'

from sensor.saveServer import SaveServer
from sensor.arduDriver import ArduDriver
from sensor.gy65_temp import Gy65_temp
from sensor.dht11 import Dht11
from sensor.sensorContainer import SensorContainer

saveSarver = SaveServer()
arduDriver1 = ArduDriver("ardu1")
#arduDriver2 = ArduDriver("ardu2")
gy65_temp1 = Gy65_temp("Gy65_temp1", "Temperatura", "1", 1,"ardu1")
dht11_hum1 = Dht11("Dht11_hum1", "Humedad", "1", 1,"ardu1")
s = SensorContainer({gy65_temp1.id: gy65_temp1,dht11_hum1.id:dht11_hum1}, "SensorContainer1",5.0)
