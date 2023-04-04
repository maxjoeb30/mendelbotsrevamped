
#Import necessary packages
import pyrosim.pyrosim as pyrosim



length = 1
width = 1
height = 1
    #
x = .5
y = .5
z = .5


#Function that:
 #Defines the file output where the world information is storedgit
 #Ends the generation process by closing the SDF file

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.End()

#Function that:
#Defines an output (URDF) file for storing the robot's body
#Generates the cubes torso, backleg, and frontleg
#Generates the first cube and first joint using absolute positioning
#Generates the resulting cubes and joints using relative positioning that connect to the last upstream joint
#Ends pyrosim simulation

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos= [0, 0, 1.5], size = [length,width,height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [.5,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos= [.5,0,-.5], size = [length,width,height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [-.5,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos= [-.5,0,-.5], size = [length,width,height])


    pyrosim.End()



#Create a new function to generate a robot body
def Generate_Body():

    #Open the urdf file to store the robot
    pyrosim.Start_URDF("body.urdf")
    #Create the robot's physical parts
    pyrosim.Send_Cube(name="Torso", pos= [0, 0, 1.5], size = [length,width,height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [.5,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos= [.5,0,-.5], size = [length,width,height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [-.5,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos= [-.5,0,-.5], size = [length,width,height])


def Generate_Brain():

    #Open the urdf file to store the robot' brain
    pyrosim.Start_NeuralNetwork("brain.nndf")
    #Create the brain's parts
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")





    pyrosim.End()




#Call the respective functions
Create_World()
Generate_Body()
Generate_Brain()
Create_Robot()



#Generate cubes in the world with variables as l,w,h and position variables as x,y,z

#First box variables



#Cube generation 1
#pyrosim.Send_Cube(name="Box", pos= [x, y, z], size = [length,width,height])

#Cube generation 2
#pyrosim.Send_Cube(name="Box2", pos= [x2, y2, z2], size = [length2,width2,height2])


#Procedural generation of links
#forlistgenloop = 10
#forlistgenloop2 = 5
#forlistgenloop3 = 5
#for i in range(forlistgenloop3):
    #for i in range(forlistgenloop2):

        #Reset the length, width, height fields    
        #length = 1
        #width = 1 
        #height = 1
        #z = 1

        #for i in range(forlistgenloop):
            #pyrosim.Send_Cube(name="Box", pos= [x, y, z], size = [length,width,height])
            #z = z + 1
            #length = length * .9
            #width = width * .9
            #height = height * .9

        #x = x + 1
    #x = 1
    #y = y + 1







