#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binary_arr = [0 for i in range(0,32)]
    binary=bin(n)
    binary_arr[-len(binary[2:]):] = binary[2:]
       
    #flipping
    for i in range(len(binary_arr)):
        if int(binary_arr[i])==0:
            binary_arr[i]=1
        elif int(binary_arr[i])==1:
            binary_arr[i]=0
        else:
            print("Error")
            
    binary_str = map(str, binary_arr)
    result_str = ''.join(s for s in binary_str)
    result_integer = int(result_str,2)
    return result_integer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
