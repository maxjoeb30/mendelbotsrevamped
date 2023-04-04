#Importing necessary packages
#import constants as c
#import pybullet as p
#import pybullet_data
#import pyrosim.pyrosim as pyrosim
#import random as r
#import numpy as numpy
#import time

from simulation import SIMULATION



#backLegSensorValues = numpy.zeros(c.emptyZeroVectorSize)
#frontLegSensorValues = numpy.zeros(c.emptyZeroVectorSize)
#targetAngles = numpy.zeros(c.emptyZeroVectorSize)

#Create a vector of motor inputs for each leg
#targetAnglesBack = (c.amplitudeBack * numpy.sin(c.frequencyBack * numpy.linspace(c.linspaceLowerBound, c.linspaceUpperBound, c.linspaceVectorSize) + c.phaseOffsetBack))
#targetAnglesFront = (c.amplitudeFront * numpy.sin(c.frequencyFront * numpy.linspace(c.linspaceLowerBound, c.linspaceUpperBound, c.linspaceVectorSize) + c.phaseOffsetFront))


#Save this vector to a file for plotting
#targetAnglesData  = "data/targetAnglesData.npy"
#numpy.save("data/targetAnglesDataBack.npy", targetAnglesBack)
#numpy.save("data/targetAnglesDataFront.npy", targetAnglesFront)


#Stepping through physics engine at a time delay with a for loop
#for i in range(c.forLoopList):
    #p.stepSimulation()

    #Records a sensor value for each leg
    #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    #Create motors for each leg
    #Backleg
    #pyrosim.Set_Motor_For_Joint(
    #bodyIndex = robotId,
    #jointName = b"Torso_BackLeg",
    #controlMode = p.POSITION_CONTROL,
    #targetPosition = targetAngles[i],
    #maxForce = c.maxForce)
    #FrontLeg
    #pyrosim.Set_Motor_For_Joint(
    #bodyIndex = robotId,
    #jointName = b"Torso_FrontLeg",
    #controlMode = p.POSITION_CONTROL,
    #targetPosition = targetAngles[i],
    #maxForce = c.maxForce)


    #time.sleep(c.timeSleep)
    

#Disconnect from the simulation and print the backLeg sensor values
#Define the variable for each leg with its path within the data subdirectory
#backLegSensorValueData = "data/backLegSensorValueData.npy"
#frontLegSensorValueData = "data/frontLegSensorValueData.npy"


#Save the data for each leg to disk
#numpy.save(backLegSensorValueData, backLegSensorValues)
#numpy.save(frontLegSensorValueData, frontLegSensorValues)


#print(backLegSensorValues)
simulation = SIMULATION()
simulation.Run()


