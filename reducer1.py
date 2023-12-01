#!/usr/bin/env python3
# import sys 


# for line in sys.stdin:
#     item,rating=line.strip().split()
#     rating=int(rating)
#     if item[-1]=="b":
#         if rating<3:
#             print(item,rating)
#     else:
#         print(item,rating)        



import sys

for code in sys.stdin:
    product, stars = code.strip().split('$')
    stars = int(stars)
    
    if product[-1] == 'r' and stars < 3:
        print(product, stars)
    elif product[-1] != 'r':
        print(product, stars)
