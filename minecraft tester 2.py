# Minecraft Teleport
import time,mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

time.sleep(3)
mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1")
time.sleep(1)
mc.player.setPos(30,40,38)
time.sleep(5)
mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1")
time.sleep(1)
mc.player.setPos(39,80,46)
