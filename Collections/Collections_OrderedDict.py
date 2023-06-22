from collections import OrderedDict
N = int(input())
sales = OrderedDict()
for i in range(N):
    item_name, item_price = input().rsplit(" ", 1)
    if item_name in  sales:
        sales[item_name] += int(item_price)
    else:
        sales[item_name] = int(item_price)
for name, price in sales.items():
    print(name, price)