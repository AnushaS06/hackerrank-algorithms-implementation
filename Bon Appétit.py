#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bAct=0
    bChar=0
    for i in range(len(bill)):
        if(i != k):
            bAct += bill[i]
        bChar += bill[i]
    bAct=int(bAct/2)
    bChar=int(bChar/2)
    if(bAct==b):
        print("Bon Appetit")
    else:
        print(bChar-bAct)
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
