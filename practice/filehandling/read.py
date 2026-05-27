file_location = r"C:\Users\tatum\OneDrive\Documents\intro to programming\IntroToProgramming\practice\filehandling\sample.txt"

with open(file_location, "r") as file:
    contents = file.read()
    print(contents)

with open(file_location, "r") as file:
    lines = file.read().splitlines()
    print(lines)

with open(file_location, "r") as file:
    for line in file:
        print(line.strip())

with open(file_location, "r") as file:
    for line in file:
        print(line.strip().split(","))

