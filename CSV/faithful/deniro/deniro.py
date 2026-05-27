import csv

with open("C:\\Users\\tatum\\OneDrive\\Documents\\intro to programming\\IntroToProgramming\\CSV\\faithful\\deniro\\deniro.csv", "r") as table:
    table = csv.DictReader(table)

    movie_titles = []
    total_movies = 0 
    movie_score = []
    total_score = 0
    years = []
    total_years = 0 
    for row in table:
        movie_titles.append(row["Title"])
        total_movies += 1
        movie_score.append(row["Score"])
        total_score += float(row["Score"])
        years.append(row["Year"])
        total_years += int(row["Year"])

    print("Deniro has been in", total_movies, "movies")
    print("the average score of his movies is",str(total_score / len(movie_score)), "out of 100.")
    print("the highest score of his movies is",str(max(movie_score)),"out of 100.", "this movie is",movie_titles[movie_score.index(max(movie_score))])
    print("the lowest score of his movies is",str(min(movie_score)),"out of 100.","this movie is",movie_titles[movie_score.index(min(movie_score))])
    print("the movie with the longest title is", max(movie_titles, key=len))
    print("the longest time between movies is", max([int(years[i]) - int(years[i-1]) for i in range(1, len(years))]), "years")
