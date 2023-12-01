#!/usr/bin/env python3
import sys 

# previtem=None
# total=0


# for line in sys.stdin:
#     item,quantity=line.strip().split()
#     quantity=int(quantity)
#     if previtem==item:
#         total=total+quantity
#     else:
#            if (previtem):
#                  print(previtem,total)
#            previtem=item
#            total=quantity    
# if (previtem):
#     print(previtem,total,sep="\t")  


#!/usr/bin/env python3
import sys

prev_product = None
balance = 0

for line in sys.stdin:
    product, amount = line.strip().split()
    product = product.split('+')[0]
    amount = int(amount)
    
    if prev_product != product:
        if prev_product is not None:
            print(prev_product,balance,sep="\t")
        prev_product = product
        balance = 0
    
    balance += amount

if prev_product is not None:
    print(prev_product,balance,sep="\t")

    
    
