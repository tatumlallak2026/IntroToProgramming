num = 10
#global scope
def increase_num():
    num = 23
    print (num)
    #local scope
    #local scope can acces global scope

#global scope cannot access local scope
#EX:
#print (num_two)

increase_num()

var = 5 
def print_var():
    print (var)

print_var()

