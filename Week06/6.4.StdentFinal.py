def display_menu():
    print ("What would you like to do?")
    print("\t (a) Add a new student")
    print("\t (v) View Studen")
    print("\t (q) Quit ")
    choice = input("Type one letter (a/v/q): ")
    return choice 

def do_add(students):
    current_student = {}
    current_student["name"]= input("Enter Name: ")
    current_student["modules"]= read_modules()
    students.append(current_student)
    
def read_modules():
    modules =[]
    module_name= input ("\t Please enter module name (blank to quit): ").strip()
    while module_name != "":
        module = {}
        module["module"]= module_name
        module["grade"]= int(input("\t \t Grade: "))
        modules.append(module)
        module_name= input ("\t Please enter module name (blank to quit): ").strip()
    return modules

def display_modules(modules):
    print("\t Name   \t Grade")
    for module in modules:
        print (f"\t  {module['module']}   \t {module['grade']}")

def do_view(students):
   for current_student in students:
       print(current_student["name"])
       display_modules(current_student["modules"])
    
students=[]
choice = display_menu()

while (choice != "q"):
        if choice == "a":
            do_add(students)
        elif choice == "v":
            do_view(students)
        else:
            print ("\n\n Please select either a,v or q: ")
        choice = display_menu()
    
print("You choose to quit")