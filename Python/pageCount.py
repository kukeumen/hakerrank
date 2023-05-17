#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    if p%2==0:
        goal=p
    elif p%2!=0:
        goal=p-1
         
    for i in range(n):
        left = 2*i
        if left==goal:
            from_front = i
    
    for j in range(n):
        if n%2==0:
            n=n
        elif n%2!=0:
            n=(n-1)
        left = n-(2*j)
        if left==goal:
            from_back = j
    
    if from_front>=from_back:
        result=from_back
    elif from_front<from_back:
        result=from_front
    else:
        print("Error")
    
    return result
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
