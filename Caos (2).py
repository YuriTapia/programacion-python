#Yoritzkiri Tapia Mateo
#Laboratorio 2
#Ejercicio 3
import math
T= [[1,2,4,1],[1,3,1,1]]
Po=[2,2]
Salida=[[],[]]
for i in range (11):
    num= math.random(0,3)
    ver=[T[0][num],T[1][num]]
    Pmx=(Po[0]-ver[0])/2
    Pmy=(Po[1]-ver[1])/2
    Salida[0].append(Pmx)
    Salida[1].append(Pmy)
