import math
import os
import random
import re
import sys
def countApplesAndOranges(s, t, a, b, apples, oranges):
    totalapples=0
    totalorange=0
    for i in range(len(apples)):
        if s<= a + apples[i]<=t:
            totalapples+=1
    for i in range(len(oranges)):
        if s<= b + oranges[i]<=t:
            totalorange+=1
    print("En total han caido", str(totalapples),"manzanas")
    print("En total han caido", str(totalorange),"narajas")

def listaAleatorios(n,a,b): #distancia de las manzanas y naranjas aleatorias
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(a,b)
      return lista

if __name__ == '__main__':
    s = 4
    t = 8
    a = 2
    b = 10
    m = 7
    n = 5
    apples = listaAleatorios(2,a,b)
    oranges = listaAleatorios(2,a,b)
    countApplesAndOranges(s, t, a, b, apples, oranges)
