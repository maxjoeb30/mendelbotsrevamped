#Importing necessary packages
import pybullet as p
import time


#Setting up the physics client, connect to simulation
physicsClient = p.connect(p.GUI)

#Stepping through physics engine at a time delay with a for loop

#Create a list for use in the for loop
forlooplist = 1000

for i in range(forlooplist):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
    
#Disconnect from the simulation
p.disconnect()



