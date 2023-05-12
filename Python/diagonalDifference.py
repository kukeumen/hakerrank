#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    first_diagonal=0
    for i in range(len(arr)):
      temp_arr = arr[i]
      first_diagonal += temp_arr[i]
    print(first_diagonal)

    second_diagonal=0
    for j in range(len(arr)):
      temp_arr = arr[j]
      second_diagonal += temp_arr[len(arr)-1-j]
    return abs(first_diagonal-second_diagonal)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        
    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
