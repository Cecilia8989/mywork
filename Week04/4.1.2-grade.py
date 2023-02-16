percentage_rounded= float(input("Please enter the percentage: "))

if percentage_rounded <0 or percentage_rounded >100:
    print("Please enter a number between 0 and 100")
elif percentage_rounded <= 40:
    print("Fail")
elif  percentage_rounded < 49.5:
    print ("Pass")
elif percentage_rounded < 59.5:
    print("Merit 2")
elif percentage_rounded < 69.5:
    print ("Merit 1")
else:
    print("Distintion")
