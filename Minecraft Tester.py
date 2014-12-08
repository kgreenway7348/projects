import time,mcpi.minecraft as minecraft # This line makes the com know its minecraft
mc = minecraft.Minecraft.create()#This connects to current game loaded up
time.sleep(4)
mc.postToChat("Hello")
