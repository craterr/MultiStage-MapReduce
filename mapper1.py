#!/usr/bin/env python3
# import sys 
# for line in sys.stdin:
#     obj = line.strip().split("\t")[:5]
#     if obj[0]=="order":
#      print(obj[3],obj[2],"a",sep=",",end=" ")
#      print(obj[4])
     
#     else:
#      print(obj[2],obj[3],"b",sep=",",end=" ")
#      print(obj[4]) 
     
    

# ## !/usr/bin/env python3
import sys
for perline in sys.stdin:
    code = perline.strip().split('\t')[:5]
    if code[0]=='order':
        print(f'{code[3]},{code[2]},o',end='$')
        print(f'{code[4]}')
    elif code[0]=='review':
        print(f'{code[2]},{code[3]},r',end='$')
        print(f'{code[4]}')