import picamera,time,json

def getPicture(n): #This function gets the photo of the person.
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (1024,728)# The resoloution
            check = False
            while check == False:
                    camera.start_preview()# When the person is not happy with the photo it will take it again.
                    filename=name+".jpeg"
                    camera.capture(filename)
                    time.sleep(2)
                    camera.stop_preview()
                    if input("Is this picture okay. Y/N") == "Y":
                        check = True
                   
                                
                        
                   

    except picamera.exc.PiCameraValueError:#Instead of crashing when the camera is unplugged it will give a user friendly message.
        print("The camera is unplugged")
        filename=""

    return filename



def getInfoProfile():#This organizes their profile and it gets the information.
        (eyecolour) = ""
        while (eyecolour) == "":
            (eyecolour) =input("What is your eye colour?")

        (name) = ""
        while (name) =="":
            (name) =input("What is your name?")

        (hat) = ""
        while (hat) == "":
            (hat) =input("Do you wear a hat?")

        (haircolour) = ""
        while (haircolour) == "":
            (haircolour) =input("What is your haircolour?")

        (gender) = ""
        while (gender) == "":
            (gender) =input("What is your gender?")

        (facial hair) = ""
        while (facial hair) == "":
            (facial hair) =input("Do you have facial hair?")

            

            
        

def saveProfile(): #This organizes and stores.
        profile = getProfile()
        with open("profile.txt",mode = "a",encoding = "utf-8") as my_file:
            for item in profile:
                my_file.write(item+",")
                my_file.write("\b\n")
                

def loadProfile():
    try:
        with open("profiles.txt",mode = "w") as p:
                  profiles = json.load(p)
    except IOError:
                  print("IO ERROR ALERT,CREATE PROFILE")#This is to stop it crashing and is more user freindly.
                  
