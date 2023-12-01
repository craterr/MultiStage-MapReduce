#!/usr/bin/env python3
# import sys 


# previtem=None
# prevvalue=0

# for line in sys.stdin:
# 	item,value=line.strip().split()
# 	value=int(value)
# 	if item[-1]=="r":
# 		print(item,value,prevvalue)
# 	previtem=item	
# 	prevvalue=value 


##!/usr/bin/env python3
import sys
old_product = None
old_value = 0
for code in sys.stdin:
    full_line = code.strip().split()
    product = full_line[0]
    stars = int(full_line[1])
    # print(stars)
    # if product[-1]=='r':
    #     print(product,stars,old_value)
    # old_product=product
    # old_value=stars
    if product[-1].endswith('r'):
        print(product,stars,old_value)
    old_product=product
    old_value=stars
