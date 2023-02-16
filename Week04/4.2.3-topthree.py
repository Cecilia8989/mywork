import random

range_from = 0
range_to = 100
how_many = 10
top = 3

y=[]
for i in range(0,how_many):
    y.append(random.randint(range_from,range_to))
print(f"10 Random number: \t {y}")

top_three = sorted(y, reverse=True)

print(f"The top one are \t {top_three[0:top]}")


