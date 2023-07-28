films = ['Die Hard', 'Back to the Future', 'Taxi Driver', 'Leon', 'Bohemian Rhapsody', 'Sin City', 'Memento', 'The Departed', 'Village']

n = int(input("How many films do you want to add? "))

favorites = []

for i in range(n):
    
    movie = input("Enter movie name: ")
    
    if movie in films:
        
        favorites.append(movie)
    else:
        
        print("Error: We don't have a {} movie :(".format(movie))

print("Your list of favorite films:", ", ".join(favorites))