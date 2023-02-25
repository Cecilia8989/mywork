student = { 
    "Student" : "Mary",
    "Modules" : [
               {
                   "course_name" : "Programming ",
                   "grade" : 65
               },
               {
                   "course_name" : "Computing ",
                    "grade" : 70
               }
           ]
        }

print("Student : {}".format(student["Student"]))
for n in student["Modules"]:
    print ("\t {} \t:  {} ".format(n["course_name"], n["grade"]))
