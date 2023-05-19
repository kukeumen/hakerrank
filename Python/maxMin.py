#https://walk-through-me.tistory.com/19
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    minima = sum(arr)
    for i in range(len(arr)-k+1):
        unfairness = arr[i+k-1]-arr[i]
        if unfairness == 0:
            minima = 0
        if minima > unfairness:
            minima = unfairness
    return minima

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
