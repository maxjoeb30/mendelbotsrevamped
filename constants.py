#Import necessary packages from simulate.py
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random as r
import numpy as numpy
import time





#Create a list of variables from simulate.py
gravityUpperBound = 0.0
gravityLowerBound = -9.8

forLoopList = 1000

emptyZeroVectorSize = 1000

linspaceLowerBound = 0
linspaceUpperBound = 2*numpy.pi
linspaceVectorSize = 1000

amplitudeBack = numpy.pi/4
frequencyBack = 20
phaseOffsetBack = 0

amplitudeFront = numpy.pi/4
frequencyFront = 10
phaseOffsetFront = 0

maxForce = 60

timeSleep = 1/60





