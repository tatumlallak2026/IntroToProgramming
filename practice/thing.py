def better_than_average(class_points, your_points):
    count = len(class_points)
    total = sum(class_points)
    if count/total >= your_points:
        return False
    else:
        return True
    

print(better_than_average(50, 60))