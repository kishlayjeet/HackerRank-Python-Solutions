#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    a = datetime.strptime(t1, "%a %d %b %Y %X %z")
    b = datetime.strptime(t2, "%a %d %b %Y %X %z")
    c = (abs(int((a - b).total_seconds())))
    return str(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
