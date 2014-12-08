import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

for block in (0,2,4,6,8,10):
    mc.setBlock(0,30,block,22)
    mc.postToChat(block)
    time.sleep(2)

for name in ("harry","bethany","jo","katy"
             mc.postToChat(name)
             time.sleep(2)

