
#Import necessary packages
import pyrosim.pyrosim as pyrosim

#Define the file output where the world information is stored
pyrosim.Start_SDF("boxes.sdf")

#Generate cubes in the world with variables as l,w,h and position variables as x,y,z

#First box variables
length = 1
width = 1
height = 1
#
x = 1
y = 1
z = .5


#Cube generation 1
#pyrosim.Send_Cube(name="Box", pos= [x, y, z], size = [length,width,height])

#Cube generation 2
#pyrosim.Send_Cube(name="Box2", pos= [x2, y2, z2], size = [length2,width2,height2])


#Procedural generation of links
forlistgenloop = 11
forlistgenloop2 = 6
forlistgenloop3 = 6
for i in range(forlistgenloop3):
    for i in range(forlistgenloop2):

        #Reset the length, width, height fields    
        length = 1
        width = 1 
        height = 1

        for i in range(forlistgenloop):
            pyrosim.Send_Cube(name="Box", pos= [x, y, z], size = [length,width,height])
            z = z + 1
            length = length * .9
            width = width * .9
            height = height * .9

        x = x + 1 
    y = y + 1







#End the generation process by closing the SDF file
pyrosim.End()