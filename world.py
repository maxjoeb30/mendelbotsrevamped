import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random as r
import numpy as numpy
import time





class WORLD:
    def __init__(self):
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")