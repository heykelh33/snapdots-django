__author__ = 'guille'
from abc import ABCMeta, abstractmethod


class Sensor(object):
    __metaclass__ = ABCMeta

    def __init__(self, id, variable, type, gpiopin,arduDriver):
        self.id = id
        self.variable = variable
        self.type = type
        self.gpiopin = gpiopin
        self.arduDriver= arduDriver

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def recive(self,data):
        pass

    def getId(self):
        return self.id

    def getVariable(self):
        return self.variable

    def getType(self):
        return self.type

    def getGpiopin(self):
        return self.gpiopin

    def getArduDriver(self):
        return  self.arduDriver