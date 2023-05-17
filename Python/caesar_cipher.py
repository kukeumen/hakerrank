#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result_string=list()
    for i in range(len(s)):
        if ord(s[i])>=65 and ord(s[i])<91:
            if ord(s[i])+k>90: 
                index = 65+((ord(s[i])-ord('A')+k)%26)
                character=chr(index)
            else: 
                character = chr(ord(s[i])+k)
        elif ord(s[i])>=97 and ord(s[i])<123:
            if ord(s[i])+k>122: 
                index = 97+((ord(s[i])-ord('a')+k)%26)
                character=chr(index)
            else: 
                character = chr(ord(s[i])+k)
        else:
            character = s[i]
        result_string.append(character)
    result = ''.join(result_string)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
