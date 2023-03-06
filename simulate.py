#Importing necessary packages
import pybullet as p
import pybullet_data
import time


#Setting up the physics client, connect to simulation
physicsClient = p.connect(p.GUI)

#Offer access to pybullet data
p.setAdditionalSearchPath(pybullet_data.getDataPath())


#Create a list for use in the for loop
forlooplist = 1000

#Setting specifics of the environment
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")


#Read in the simulated world environment from box.sdf
p.loadSDF("box.sdf")


#Stepping through physics engine at a time delay with a for loop
for i in range(forlooplist):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
    
#Disconnect from the simulation
p.disconnect()



