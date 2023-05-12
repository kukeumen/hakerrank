#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.lower()
    result = "pangram"
    alphabet_list = list(ascii_lowercase)
    alphabet_list.append(' ')
    for alphabet in alphabet_list:
        if alphabet not in s:
            result = "not pangram"
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
