#SOS flasher by kathryn Greenway + alphabet

import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BOARD) #Set the pin numbering

GPIO.setup(11,GPIO.OUT)

#Function Definition

def dot():
	GPIO.output(11,True)
	time.sleep(1) 		
	GPIO.output(11,False)
	time.sleep(1)


def dash():
        GPIO.output(11,True)
	time.sleep(3)
	GPIO.output(11,False)
	time.sleep(3)


def morse(letter):
        if letter == "a":
                dot()
                dash()
        elif letter == "b":    
                dash()
                dot()
                dot()
                dot()
        elif letter == "c":
                dash()
                dot()
                dash()
                dot()
        elif letter == "d":
                dash()
                dot()
                dot()
        elif letter == "e":
                dot()
        elif letter == "f":
                dot()
                dot()
                dash()
                dot()
        elif letter == "g":
                dash()
                dash()
                dot()
        elif letter == "h":
                dot()
                dot()
                dot()
                dot()
        elif letter == "i":
                dot()
                dot()
        elif letter == "j":
                dot()
                dash()
                dash()
                dash()
        elif letter == "k":
                dash()
                dot()
                dash()
        elif letter == "l":
                dot()
                dash()
                dot()
                dot()
        elif letter == "m":
                dash()
                dash()
        elif letter == "n":
                dash()
                dot()
        elif letter == "o":
                dash()
                dash()
                dash()
        elif letter == "p":
                dot()
                dash()
                dash()
                dot()
        elif letter == "q":
                dash()
                dash()
                dot()
                dash()
        elif letter == "r":
                dot()
                dash()
                dot()
        elif letter == "s":
                dot()
                dot()
                dot()
        elif letter == "t":
                dash()
        elif letter == "u":
                dot()
                dot()
                dash()
        elif letter == "v":
                dot()
                dot()
                dot()
                dash()
        elif letter == "w":
                dot()
                dash()
                dash()
        elif letter == "x":
                dash()
                dot()
                dot()
                dash()
        elif letter == "y":
                dash()
                dot()
                dash()
                dash()
        elif letter == "z":
                dash()
                dash()
                dot()
                dot()
                
        
        
        


                
                
                

        elif letter == "        
                

            
