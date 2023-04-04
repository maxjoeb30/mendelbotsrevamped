import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random as r
import numpy as numpy
import time

from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

#Constructor for the robot class
class ROBOT:
    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")

#Method to initialize sensors
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
        


    def Sense(self, time):
        for i in self.sensors.values():
           #Get each value in the list of sensor values at each time step 
           i.Get_Value(time)

    def Think(self, time):
        self.nn.Update()
        self.nn.Print()

    def Act(self, time):
        for i in self.motors.values():
            i.Set_Value(time, self.robotId)


    
