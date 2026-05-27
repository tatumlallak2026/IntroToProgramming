import csv

with open("C:\\Users\\tatum\\OneDrive\\Documents\\intro to programming\\IntroToProgramming\\CSV\\faithful\\census\\occupation-2018-census-csv.csv", "r", encoding="utf-8") as file:
    table = csv.DictReader(file)

    occupations = []
    populations = []
    codes = []
    total_population = 0
    total_jobs = 0

    for row in table:         
        occupations.append(row["Occupation"])
        populations.append(int(row["Population"]))
        codes.append(row["Code"])

    print("the most popular occupation is: ", occupations[populations.index(max(populations))], "with a population of: ", max(populations))
    print("the least popular occupation is: ", occupations[populations.index(min(populations))], "with a population of: ", min(populations))
    print("the total number of Grape Growers is: ", populations[occupations.index("Grape Grower")])
    print("the job with 14298 people is: ", occupations[populations.index(14298)])
    print("the job with code 451311 is: ", occupations[codes.index("451311")])
    print("the top 5 most popular occupations are: ", occupations[populations.index(max(populations))], ", ", occupations[populations.index(sorted(populations)[-2])], ", ", occupations[populations.index(sorted(populations)[-3])], ", ", occupations[populations.index(sorted(populations)[-4])], ", ", occupations[populations.index(sorted(populations)[-5])])