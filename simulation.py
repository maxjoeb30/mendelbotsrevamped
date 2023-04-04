#Importing necessary packages
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random as r
import numpy as numpy
import time
from world import WORLD
from robot import ROBOT



class SIMULATION:
    def __init__(self):

        #Setting up the physics client, connect to simulation
        physicsClient = p.connect(p.GUI)

        #Offer access to pybullet data
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        #Setting specifics of the environment
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
    
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        for t in range(c.forLoopList):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think(t)
            self.robot.Act(t)




            time.sleep(c.timeSleep)

            #print(t)

    def __del__(self):

        p.disconnect()


    