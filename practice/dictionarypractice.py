student = {"name": "Alice", 
           "age": str(16), 
           "grade": "A"}

print(student["name"] + " has an " + student["age"])

print("but now. . . ")

del(student.pop["grade"])

student["grade"] = "A+"

print("grade")