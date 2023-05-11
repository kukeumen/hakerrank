#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    length = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for i in range(length):
        item = arr[i]
        if item > 0 :
            positive+=1
        elif item < 0:
            negative+=1
        elif item == 0:
            zero+=1
        else:
            print("ERROR Occured")
    print(positive/length)
    print(negative/length)
    print(zero/length)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
