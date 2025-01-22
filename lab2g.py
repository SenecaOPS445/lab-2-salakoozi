#!/usr/bin/env python3
#Author: Sohail Alakoozi
#Author ID: 118320217
#Date Created: 2025/01/22

import sys

if len(sys.argv) == 1:
    timer = 3

elif len(sys.argv) == 2:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1


print('blast off!')


