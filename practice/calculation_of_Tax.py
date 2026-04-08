
item = input()

def applecost():
    return .99

def rate():
    return 6.875

def price():
    return applecost()

def total():
    return rate() * price()

store = {
    "apple": 0.99,
    "banana": 0.59
    ,
}

print(store[item])

print(total())