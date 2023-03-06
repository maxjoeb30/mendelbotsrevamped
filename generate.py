
#Import necessary packages
import pyrosim.pyrosim as pyrosim

#Define the file where the world information is stored
pyrosim.Start_SDF("box.sdf")

#Generate a cube in the world
pyrosim.Send_Cube(name="Box", pos= [0,0,0.5] , size = [1,1,1])



#End the generation process by closing the SDF file
pyrosim.End()