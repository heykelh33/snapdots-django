__author__ = 'root'

from dataJson import DataJson

class ResponseData(DataJson):
    def __init__(self, idSensor, variable, value,time):
        self.idSensor = idSensor
        self.variable = variable
        self.value = value
        self.time = time

    def getIdSensor(self):
        return self.idSensor

    def getVariable(self):
        return self.variable

    def getValue(self):
        return self.value

    def getTime(self):
        return self.time