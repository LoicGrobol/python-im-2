import sys
import math

while True:
    max_h = -1
    target = None
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > max_h:
            max_h = mountain_h
            target = i

    print(target)
