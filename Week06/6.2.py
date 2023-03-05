def make_your_choice():
    print ("What would you like to do?")
    print("\t (a) Add a new student")
    print("\t (v) View Studen")
    print("\t (q) Quit ")
    choice = input("Type one letter (a/v/q): ")
    return choice 

choice= make_your_choice()

def doAdd():
    print("in adding")

def doView():
    print("in viewing")

while choice != 'q':
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice != "q":
        print ("Please enter (a/v/q)")
    choice= make_your_choice()
        

print ("you have select quit")
    
