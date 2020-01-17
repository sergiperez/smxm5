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
    requested = request.split("/")
    ipAnswer = answer.split(".")
    mask = requested[1]
    ip = requested[0].split(".")
    indexFinal = int(int(mask) / 8)
    if len(ip) != len(ipAnswer) or ip == ipAnswer or ip[0:indexFinal] != ipAnswer[0:indexFinal]:
        return False
    broadCast = False
    network = False
    while(indexFinal < len(ip)):
        if (ipAnswer[indexFinal] == "255"):
            broadCast = True
        elif (ipAnswer[indexFinal] == "0"):
            network = True
        else:
            network = False
            broadCast = False
            indexFinal = len(ip)
        indexFinal = indexFinal + 1
    if (broadCast):
        return False
    elif (network):
        return False
    #TODO Comprovar que no hi ha broadcast o xarxa
    #TODO Preguntar classe, ip's de xarxa, boradcast, màscares que permet que es vegin
    return True


masks = [8,16,24]
points = 0
speedInitial = 20
speed = speedInitial
gameOver = False
player = str(subprocess.check_output("whoami"))

while not(gameOver):
    print("IP ATTACK")
    print("Hola  "+player[2:len(player)-3]+" portes "+str(points)+" punts")
    timer = threading.Timer(speed, timeOver)
    timer.start()
    ipRequest = str(random.randrange(1,223))+"."+str(random.randrange(1,223))+"."+str(random.randrange(1,223))+"."+str(random.randrange(1,223))+"/"+str(masks[random.randrange(0,3)])
    print("Tens "+str(speed)+" segons per respondre")
    ipAnswer = input("Entra una ip vàlida per a PC de la mateixa xarxa "+ipRequest+":  ")
    while not(checkIP(ipRequest,ipAnswer)):
        points = points - 1
        ipAnswer = input("Error! Torna a provar-ho ")
    timer.cancel()
    points = points + 1
    speed = speedInitial - min(math.floor(points/5),7)
    os.system("clear")
