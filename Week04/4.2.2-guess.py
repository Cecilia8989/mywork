y = 30
x = int(input("Enter a number: "))
while x != y:
    if x < y:
        print ("too low")
    else:
        print ("Too hight")
    x = int(input("Enter a number: "))
print("Weel done, you entered", x)