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


if __name__ == '__main__':
    s = 0
    t = 10
    a = 2
    b = 8
    m = 7
    n = 5
    apples = [4, 5]
    oranges = [1,4]
    countApplesAndOranges(s, t, a, b, apples, oranges)
