""" Problem description
Given five positive integers, find the minimum and maximum values that can be
alculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

[Example]
arr = [1,3,5,7,9]
The minimums sum is
1+3+5+7 = 16 and the
maximum sum is
3+5+7+9 = 24.
The function prints
16 24

"""

#!/bin/python3
import copy

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    max_value = 0
    min_value = sum(arr)
    for i in range(len(arr)):
        temp_arr = copy.deepcopy(arr)
        temp_arr.remove(arr[i])
        temp_value = sum(temp_arr)
        if temp_value > max_value:
            max_value = temp_value
        if temp_value < min_value:
            min_value = temp_value
    
    print(f'{min_value} {max_value}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
