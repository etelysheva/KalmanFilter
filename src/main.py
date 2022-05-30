import kalmanfilter as kf
import time
import sys
import os
import random
import threading
import math

import numpy
import matplotlib

def _load_data():
    lines = [line.rstrip('\n') for line in open("data.txt")]
    data = []
    for line in range(0, len(lines)):
        data.append(list(map(float, lines[line].split(' '))))
    return data


data = _load_data()
output = kf.kalmanFilter(data)
kf.plot(data, output)
