#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_chars:
        if count > 1:
            print(f"{char} {count}")
 
