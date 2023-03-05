def make_your_choice():
    print ("What would you like to do?")
    print("\t (a) Add a new student")
    print("\t (v) View Studen")
    print("\t (q) Quit ")
    choice = input("Type one letter (a/v/q): ")
    return choice 

choice= make_your_choice()
print(f"you chose {choice}")