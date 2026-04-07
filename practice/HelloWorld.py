name = "tate"
age = 18
print("Name:", name, "Age:", age)
password = "mathias123"
input_password = input("Enter password: ")
if input_password == password:
    print("Access granted") 
    print("welcome:", name)
else:
    print("Access denied")
