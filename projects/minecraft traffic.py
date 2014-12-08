import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time

mc.setBlocks(3.3,0.0,26.6,-3.6,3.0,32.3,20)

mc.setBlocks(2.5,1.0,27.7,-2.5,3.0,31.4,8)

#destroying blocks

while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    block = 0
    mc.setBlocks(x-1,y,z-1,x+1,y+1,z+1,0)
    time.sleep(0.1)

#SAND RAIN!!!!!!!

import random     




