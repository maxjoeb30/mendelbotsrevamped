import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random as r
import numpy as numpy
import time





class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):

        
        if self.jointName == b'Torso_BackLeg':
        
            self.amplitudeBack = c.amplitudeBack
            self.frequencyBack = c.frequencyBack
            self.phaseOffsetBack = c.phaseOffsetBack    

            self.motorValues = (self.amplitudeBack * numpy.sin(self.frequencyBack * numpy.linspace(c.linspaceLowerBound, c.linspaceUpperBound, c.linspaceVectorSize) + self.phaseOffsetBack))

        
        if self.jointName == b'Torso_FrontLeg':
        
            self.amplitudeBack = c.amplitudeBack
            self.frequencyBack = .5 * c.frequencyBack
            self.phaseOffsetBack = c.phaseOffsetBack  
            
            self.motorValues = (self.amplitudeBack * numpy.sin(self.frequencyBack * numpy.linspace(c.linspaceLowerBound, c.linspaceUpperBound, c.linspaceVectorSize) + self.phaseOffsetBack))

            

        
        self.motorValues = (self.amplitudeBack * numpy.sin(self.frequencyBack * numpy.linspace(c.linspaceLowerBound, c.linspaceUpperBound, c.linspaceVectorSize) + self.phaseOffsetBack))

    def Set_Value(self, time, robot):
        
        #Create motors for each joint

        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.motorValues[time],
        maxForce = c.maxForce
        )

    def Save_Values(self):

        motorValueData = "data/motorValueData.npy"
        numpy.save(motorValueData, self.motorValues)
        