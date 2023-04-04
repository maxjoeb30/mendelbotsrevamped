
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random as r
import numpy as numpy
import time





class SENSOR():
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.emptyZeroVectorSize)

    def Get_Value(self, time):
        self.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        sensorValueData = "data/SensorValueData.npy"
        numpy.save(sensorValueData, self.values)
       


        