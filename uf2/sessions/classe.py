import threading
import random
import math
import time
import os
import subprocess

def timeOver():
    os.system("clear")
    print()
    print("GameOver")
    print("Has fet "+str(points)+" punts")
    os._exit(os.EX_OK)

def checkIP(request,answer):
    request = request.split(".")
    if (int(request[0]) < 128 and answer == "A") or (int(request[0]) > 191 and answer == "C") or (int(request[0]) >= 128 and int(request[0]) <= 191 and answer == "B"):
        return True
    return False

points = 0
speedInitial = 10
speed = speedInitial
gameOver = False
player = str(subprocess.check_output("whoami"))

while not(gameOver):
    print("CLASS IP ATTACK")
    print("Hola  "+player[2:len(player)-3]+" portes "+str(points)+" punts")
    timer = threading.Timer(speed, timeOver)
    timer.start()
    ipRequest = str(random.randrange(1,223))+"."+str(random.randrange(1,223))+"."+str(random.randrange(1,223))+"."+str(random.randrange(1,223))
    print("Tens "+str(speed)+" segons per respondre")
    ipAnswer = input("De quina classe és la IP "+ipRequest+":  ")
    if not(checkIP(ipRequest,ipAnswer)):
        points = points - 1
    else:
        points = points + 1
    timer.cancel()
    speed = speedInitial - min(math.floor(points/5),5)
    #os.system("clear")
