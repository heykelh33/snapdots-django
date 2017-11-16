#!/usr/bin/python
# -*- coding: utf-8 -*-
# ---importando modulos---------------

# import sensor
import time
import random
# #import threading
# import os
import glob
import datetime
import Pyro4
from sensorABC import Sensor
import time


# shutdown_thread = threading.Event()

class Ds18b20(Sensor):
    def __init__(self, nombre, variable, tipo, gpiopin):
        super(Ds18b20, self).__init__(nombre, variable, tipo, gpiopin)
        # os.system('modprobe w1-gpio')
        # os.system('modprobe w1-therm')
        self.ruta = "/sys/bus/w1/devices/' + '28*')[0] + '/w1_slave"  # glob.glob('/sys/bus/w1/devices/' + '28*')[0] + '/w1_slave'
        print "sensor " + self.getName() + " activado"

    def read(self):
        temperatura_ds18b20 = round(random.uniform(0, 50), 2)
        date = str(datetime.datetime.now())

        # archivo = open(self.ruta,'r')
        # lineas = archivo.readlines()
        # while lineas[0].strip()[-3:] != 'YES':
        # 	time.sleep(0.2)
        # 	lineas = archivo.readlines()
        # archivo.close()
        # posicion_t = lineas[1].find('t=')
        # if posicion_t != -1:
        #  se ejecuta si equal_pos es distinto de -1, es decir solo lee valores positivos de temperatura
        # 	temperatura_cadena = lines[1][posicion_t+2:]
        # 	#global temperatura
        # 	temperatura = float(temperatura_cadena) / 1000.0
        save_server = Pyro4.Proxy("PYRONAME:sensor.save")  # use name server object lookup uri shortcut
        # generar aleatoriamente data
        save_server.save(("Temperature", date, temperatura_ds18b20))
        return temperatura_ds18b20

    #   def hilo_temperatura_inicio(self):
    # temperatura_thread = threading.Thread(target=lectura_temperatura, args=())
    # temperatura_thread.start()

    #   def hilo_temperatura_detente(self):
    #       shutdown_thread()


while True:
    print "Start : %s" % time.ctime()
    time.sleep(5)
    d = Ds18b20("temperatura", "test", "1", 1)
    print(d.read())
