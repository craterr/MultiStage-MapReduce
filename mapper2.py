#!/usr/bin/env python3
# import sys

# for line in sys.stdin:
#     item, num = line.strip().split()
#     num = int(num)
#     print(item, num)




##!/usr/bin/env python
import sys

for line in sys.stdin:
    data = line.strip().split()
    item, num = data[0], int(data[1])
    print(item, num)
# import sys
# for code in sys.stdin:
#     val = code.strip()
#     full = code.split(' ')
#     # print(full)
#     product= full[0]
#     # print(product)
    
#     stars = int(full[1])
#     print(product,stars)
