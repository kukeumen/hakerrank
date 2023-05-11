#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[:2])
    time_format = s[-2:]
    if hour==12:
        if time_format=="AM":
            result_hour= 0
        elif time_format=="PM":
            result_hour=12
        else:
            print("Error")
    elif hour!=12:
        if time_format=="PM":
            result_hour = hour+12
        elif time_format=="AM":
            result_hour = hour
        else:
            print("Error")
    else:
        print("Error")
    
    if result_hour < 10:
        result_hour = "0"+str(result_hour)
        
    result = str(result_hour)+s[2:-2]

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
