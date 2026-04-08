

x = input("enter 1st number: ")
if x.isdigit() == False:
        print ("invalid input") 

y = input("enter 2nd number: ")
if y.isdigit() == False:
        print ("invalid input")
#reciving data from user

opperation = input("enter operation: ")
#asking for opperation

if opperation == "+":
    print (int(x)+int(y))
elif opperation == "-":
    print (int(x)-int(y))
elif opperation == "*":
    print (int(x)*int(y))
elif opperation == "/":
    print (int(x)/int(y))
elif opperation == "^":
    print (int(x)**int(y))
elif opperation == "abs":
    print (abs(int(x)))
    print (abs(int(y)))
elif opperation == "floor":
     print (int(x)//int(y))
elif opperation == "mod":
    print (int(x)%int(y))
#opperation selection and calculation

