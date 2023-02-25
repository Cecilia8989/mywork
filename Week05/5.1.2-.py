import random
x = []

for n in range(0,10):
    x.append(random.randint(0,100))
print("Queue is {}".format(x))

while len(x) != 0:
    current_number=x.pop(0)
    print ("Current number is {} and the queue is {}".format(current_number, x))
print ("The queue is now empty")