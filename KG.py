import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x+2,y,z,x+2,y+6,z,35,5)
mc.setBlocks(x+7,y+1,z,x+7,y+5,z,35,5)
mc.setBlocks(x+8,y,z,x+10,y,z,35,5)
mc.setBlocks(x+8,y+6,z,x+10,y+6,z,35,5)
mc.setBlock(x+11,y+5,z,35,5)
mc.setBlocks(x+10,y+2,z,x+11,y+2,z,35,5)
mc.setBlock(x+11,y+1,z,35,5)

def w(x,y,z,colour):
    mc.setBlocks(x,y,z,y+5,z,35,8)
    mc.setBlocks(x+2,y+1,z,x+2,y+6,z,35,8)
    mc.setBlocks(x+6,y+1,z,x+6,y+6,z,35,8)
    mc.setBlocks(x+4,y+1,z,x+4,y+3,z,35,8)
    mc.setBlock(x+3,y,z,35,8)
    mc.setBlock(x+5,y,z,35,8)

w(10,10,10,10)
    
