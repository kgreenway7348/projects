
import mcpi.minecraft as minecraft,time,random
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0)

for b in range(21,6,-2):
    mc.postToChat(b)
    mc.setBlock(0,b,0,35,b)
    time.sleep(2)
    
