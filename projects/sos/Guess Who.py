import picamera,time

def getPicture(name):
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (1024,728)
            check = False
            while check == False:
                    camera.start_preview()
                    filename=name+".jpeg"
                    camera.capture(filename)
                    time.sleep(2)
                    camera.stop_preview()
                    if input("Is this picture okay. Y/N") == "Y":
                        
                       check = True

    except picamera.exc.PiCameraValueError:
        print("The camera is unplugged")
        filename=""

    return filename

def getChatProfile():
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
    
