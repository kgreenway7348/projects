import time
import picamera

Name = ""
while Name =="":
    Name = input("What is your name?")
print("Good Morning"+  Name)
time.sleep(1)
print("Get ready for a photo!)

    

with picamera.PiCamera() as camera:
    camera.resolution = (1024,768)
    camera.start_preview()
    time.sleep(2)

