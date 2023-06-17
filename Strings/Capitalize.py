#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    lst = s.split()
    cap_name = s
    for name in lst:
         cap_name = cap_name.replace(name, name.capitalize())
    return cap_name
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
