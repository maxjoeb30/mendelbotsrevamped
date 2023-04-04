#Import necessary packages
import matplotlib.pyplot as mp
import numpy as numpy

#Load leg and motor data from subdirectory data
#Leg data
#backLegSensorValues = numpy.load("data/backLegSensorValueData.npy")
#frontLegSensorValues = numpy.load("data/frontLegSensorValueData.npy")

#Motor
targetAnglesDataBack = numpy.load("data/targetAnglesDataBack.npy")
targetAnglesDataFront = numpy.load("data/targetAnglesDataFront.npy")

#Print and plot data for visualization
#print(backLegSensorValues)
#print(frontLegSensorValues)
#print(targetAnglesData)



#mp.plot(frontLegSensorValues, label = "Front Leg Data") 
#mp.plot(backLegSensorValues, label = "Back Leg Data")
mp.plot(targetAnglesDataBack, label = "Target Angle Data Back")
mp.plot(targetAnglesDataFront, label = "Target Angle Data Front")
#Include the show method to send each dataset to the graph as visual data
#Include a legend
mp.legend()
mp.show()
