import time,random,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

while True: # Loops it while true.
    pos = mc.player.getPos() # Finds the players position 
    x = int(pos.x) #The int makes the float and interger
    y = pos.y
    z = int(pos.z)
    xg = random.randint(x-10,x+10)
    yg = y + 50
    zg = random.randint(z-10,z+10)
    
    gravel = 13
    
    mc.setBlock(xg,yg,zg,13)
    time.sleep(0.2)
    
    

    
    
