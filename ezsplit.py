#!/bin/env/python3

import fileinput

for line in fileinput.input():
    arrs = line.split(",")

    print(arrs[0].lower().replace(' ',''))
