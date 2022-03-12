import pyfiglet
import sys

# Generate banner and print
ascii_banner = pyfiglet.figlet_format("Lyrics Generator")
print(ascii_banner)

# User selection Menu
print("Welcome to Lyrics Generator, select a genre of music you'd like generate lyrics for: ")

# Print list of available genres
genres = ["Country", "Pop", "R-B", "Rap", "Rock", "Metal"]
for genre in genres:
    print(genre)
print("Type \"quit\" to exit.\n")

# Get user input
user_input = input("Genre: ")

# Make user input case insensitive
user_input = user_input.lower()
genre_lookup = [x.lower() for x in genres] 

# Generate lyrics, exit, or user-friendly error message when genre not found
while user_input != "quit":
    if user_input in genre_lookup:
        print("Genre found!")
        break
    elif user_input == "quit":
        sys.exit()
    else:
        user_input = input("Genre not found. Please choose a genre on the list: ")






