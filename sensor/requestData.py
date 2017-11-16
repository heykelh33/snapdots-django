__author__ = 'root'

from dataJson import DataJson

class RequestData(DataJson):
    def __init__(self, idSensorContainer, idSensor, cmd,time):
        self.idSensorContainer = idSensorContainer
        self.idSensor = idSensor
        self.cmd = cmd
        self.time = time

    def getIdSensorContainer(self):
        return self.idSensorContainer

    def getIdSensor(self):
        return self.idSensor

    def getCmd(self):
        return self.cmd

    def getTime(self):
        return self.time
# import datetime
# data = RequestData(1,1,'d',datetime.datetime.now())
# json = data.asJson()
# print(json)
# decodeJson = DataJson.jsonToObj(json)
# print decodeJson.getTime()
