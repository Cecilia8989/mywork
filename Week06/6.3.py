
def read_modules():
    
    x = 0
    for x in range (0,2):
        modules = []
        module = {}
        module_name= input ("Module name: ")
        module_grade= input ("Grade: ") 
        module["Module"]=module_name
        module["Grade"]=module_grade
        modules.append(module)
    return modules
   
print(read_modules())

 