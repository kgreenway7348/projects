import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()


pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x+2,y+8,z,35,6)#This part is the ears of the Invader.
mc.setBlock(x+8,y+8,z,35,6)
mc.setBlock(x+3,y+7,z,35,6)
mc.setBlock(x+7,y+7,z,35,6)
mc.setBlocks(x+2,y+6,z,x+8,y+6,z,35,6)#This is the main body including the eyes.
mc.setBlocks(x+1,y+5,z,x+2,y+5,z,35,6)
mc.setBlocks(x+4,y+5,z,x+6,y+5,z,35,6)
mc.setBlocks(x+8,y+5,z,x+8,y+5,z,35,6)
mc.setBlocks(x,y+4,z,x+10,y+4,z,35,6)
mc.setBlock(x+y+3,z,35,6)
mc.setBlocks(x,y+3,z,x+8,y+3,z,35,6)
mc.setBlock(x+10,y+3,z,35,6)#The feet of the invader.
mc.setBlock(x+2,y+1,z,35,5)
mc.setBlock(x+2,y+2,z,35,6)
mc.setBlock(x+8,y+2,z,35,6)
mc.setBlock(x+10,y+2,z,35,6)
mc.setBlock(x+3,y+1,z,35,6)
mc.setBlock(x+4,y+1,z,35,6)
mc.setBlock(x+6,y+1,z,35,6)
mc.setBlock(x+7,y+1,z,35,6)
