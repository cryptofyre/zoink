# Allen can't speak proper english edition.
# Now with more autism!
# and really bad story line
import os
import time
import wget
# Check version for updates. If updates are present they will install here.
print("FireUpdater v3")
print("Grabbing version info...")
os.system("python -m wget -O latest.txt https://raw.githubusercontent.com/iiFir3z/zoink/windows/latest.txt")
currentopen = open("ver.txt", "r")
currentver = currentopen.read()
latestopen = open("latest.txt", "r")
latestver = latestopen.read()
if currentver == latestver :
  print("Up to date! Continuing with program.")
  os.system("cls")
  os.system("python game.py")
else:
  print("Version is out of date!")
  os.system("python -m wget -O ver.txt https://raw.githubusercontent.com/iiFir3z/zoink/windows/ver.txt")
  time.sleep(2)
  print("Installing latest build of Zoink. (FireUpdater v3)")
  os.system("python -m wget -O game.py https://raw.githubusercontent.com/iiFir3z/zoink/windows/game.py")
  print("Update successfully installed. Starting application.")
  time.sleep(4)
  os.system("cls")
  # Starting application.
  os.system("python game.py")
