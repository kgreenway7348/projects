import picamera,time

def getPicture(name): #This function gets the photo of the person.
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

def getChatProfile():#This organizes their profile.
    name = ""
    while name == "":
        print("What is your name?")

    glasses =""
    while glasses == "":
        print("Do you wear glasses?")

    haircolour =""
    while haircolour ==("brown","blonde","black","red"):
        print("OK")


    def saveProfile():
        profile = getProfile()
        with open("profile.txt"),mode == "a",encoding == ("utf-8") as my_file
    for item in profile:
        my_file.write(item+",")
    my_file.write("\b\n")    
    
