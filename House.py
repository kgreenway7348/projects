import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
time.sleep(5)

def build_houses(x,y,z):
    mc.setBlocks(x+2,y,z+2,x+6,y+4,z+8,45)
    mc.setBlocks(x+3,y,z+3,x+5,y+4,z+7,0)
    mc.setBlocks(x+4,y,z+2,x+4,y+1,z+2,0)
    mc.setBlocks(x+2,y+5,z+2,x+6,y+5,z+8,35)

build_houses(x,y,z)
build_houses(20,20,20)
build_houses(40,20,20)


