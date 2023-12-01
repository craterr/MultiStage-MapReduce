#!/usr/bin/env python3
import sys 




# for line in sys.stdin:
#     item,rating,quantity=line.strip().split()
#     quantity=int(quantity)
#     item=item.split(",")
#     print(item[0],quantity)


#!/usr/bin/env python3
import sys
for code in sys.stdin:
    full_line=code.strip()
    after_split=full_line.split()
    # print(after_split)
    product = after_split[0]
    stars = int(after_split[1])
    # print(stars)
    amount = after_split[2]
    product = product.split(',')
    print(f'{product[0]}+{product[1]} {amount}')
