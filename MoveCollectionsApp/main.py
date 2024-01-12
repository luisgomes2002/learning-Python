menuPrompt = "\nEnter 'a' to add a movie, Enter 'l' to see a your movies, Enter 'f' to find a movie by title, or 'q' to quit: "
movies = []

def addMovie(): 
    title = input("Entrer the move title: ")
    director = input("Entrer the move director: ")
    year = input("Entrer the move year: ")
    
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def printMovies(movie):
	print(f"Title: {movie['title']}")
	print(f"director: {movie['director']}")
	print(f"year: {movie['year']}")

def showAllMovies():
    for movie in movies:
        printMovies(movie)

def findMovie():
    searchMove = input("Enter the move title: ")
    found = False
    for movie in movies:
        if movie['title'] == searchMove:
            printMovies(movie)
    if not found:
        print("Movie not found.")
 
userOptions = {
    "a" : addMovie,
    "l" : showAllMovies,
    "f" : findMovie
}  
   
def menu():
    selection = input(menuPrompt)
    while selection != 'q':
        if selection in userOptions:
            userSelection = userOptions[selection]
            userSelection()
        else:
            print("Unknown command, Please try again.")   
            
        selection = input(menuPrompt)

    
menu()