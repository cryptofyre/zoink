# Allen can't speak proper english edition.
# Now with more autism!
# and really bad story line
import os
import time
# Check version for updates. If updates are present they will install here.
print("FireUpdater v3")
print("Grabbing version info...")
os.system("wget -O latest.txt https://raw.githubusercontent.com/iiFir3z/zoink/master/latest.txt")
currentopen = open("ver.txt", "r")
currentver = currentopen.read()
latestopen = open("latest.txt", "r")
latestver = latestopen.read()
if currentver == latestver :
  print("Up to date! Continuing with program.")
  os.system("clear")
  os.system("python game.py")
else:
  print("Version is out of date!")
  os.system("wget -O ver.txt https://raw.githubusercontent.com/iiFir3z/zoink/master/ver.txt")
  time.sleep(2)
  print("Installing latest build of Zoink. (FireUpdater v3)")
  os.system("wget -O game.py https://raw.githubusercontent.com/iiFir3z/zoink/master/game.py")
  print("Update successfully installed. Starting application.")
  time.sleep(4)
  os.system("clear")
  # Starting application.
  os.system("python game.py")
