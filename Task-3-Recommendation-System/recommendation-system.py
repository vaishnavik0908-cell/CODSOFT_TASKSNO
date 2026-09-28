# CODSOFT Task 4 - Recommendation System

movies = {
    "Inception": ["Interstellar", "The Matrix", "The Prestige"],
    "Interstellar": ["Inception", "The Martian", "Gravity"],
    "The Matrix": ["Inception", "Avatar", "Terminator"],
    "The Prestige": ["Inception", "The Illusionist", "Memento"],
    "The Martian": ["Interstellar", "Gravity", "Apollo 13"],
    "Gravity": ["Interstellar", "The Martian", "Apollo 13"],
    "Avatar": ["The Matrix", "Guardians of the Galaxy", "Star Wars"],
    "Terminator": ["The Matrix", "Robocop", "Predator"]
}

movie = input("Enter a movie you like: ")

if movie in movies:
    print("\nRecommended movies:")

    for recommendation in movies[movie]:
        print("-", recommendation)
else:
    print("\nSorry, this movie is not in our database.")