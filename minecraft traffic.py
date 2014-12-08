import mcpi.minecraft as minecraft,time as t
mc = minecraft.Minecraft.create()

black=7
red=14
orange=1
green=5

mc.setBlock(18,0,1,35,black)
mc.setBlock(18,1,1,35,black)
mc.setBlock(18,2,1,35,black)
mc.setBlock(18,3,1,35,black)
mc.setBlock(18,4,1,35,black)
mc.setBlock(18,5,1,35,black)

while True:#loops program
    mc.setBlock(18,5,1,35,red)
    t.sleep(10)
    mc.setBlock(18,4,1,35,orange)
    t.sleep(2)
    mc.setBlock(18,5,1,35,black)
    mc.setBlock(18,4,1,35,black)
    mc.setBlock(18,3,1,35,green)
    t.sleep(10)
    mc.setBlock(18,3,1,35,black)
    mc.setBlock(18,4,1,35,orange)
