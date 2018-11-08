#!/bin/env/python3

import fileinput

for line in fileinput.input():
    arrs = line.split(",")

    code = arrs[0].lower().replace(' ','')
    section = arrs[1]

    num = 0
    while num < len(code) and ord(code[num]) in range(ord('a'),ord('z')+1):
    	num += 1

    num += 3
    code = code[0:num]

    begin = "%7s-%2s" % (code,section) 

    print(begin,end='')

    for i in range(2,9):
    	print(" %8s" % arrs[i].replace(' ','').replace('\n',''),end='')
    for i in range(13,17):
    	print(" %3s" % arrs[i].replace(' ','').replace('\n',''),end='')


    print("")
