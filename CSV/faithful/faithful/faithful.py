import csv

with open("C:\\Users\\tatum\\OneDrive\\Documents\\intro to programming\\IntroToProgramming\\CSV\\faithful\\faithful\\faithful.csv", "r") as file:
    table = csv.DictReader(file)
    
    wait_times = []
    total_wait = 0
    eruption_times = []
    total_eruption = 0
    for row in table:
        wait_times.append(row["wait"])
        total_wait += int(row["wait"])
        eruption_times.append(row["length"])
        total_eruption += float(row["length"])

    print("-------------------------------")
    print("the average eruption time is", str(total_eruption / len(eruption_times)), "minutes")
    print("the longest eruption time is" + str(max(eruption_times)), "minutes")
    print("the shortest eruption time is" + str(min(eruption_times)), "minutes")
    print("------------------------------")
    print("the shortest wait time is" + str(min(wait_times)), "minutes")
    print("the average wait time is", str(total_wait / len(wait_times)), "minutes")
    print("the longest wait time is" + str(max(wait_times)), "minutes")
    print("------------------------------")
    print("the eruption time of the longest wait time is", eruption_times[wait_times.index(max(wait_times))], "minutes")
    print("-------------------------------")

