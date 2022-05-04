# Implemented Lyrics Generator User Selection Menu by Ivan Delgado
import pyfiglet
import sys
import geniusclient
import generate
import os

# Generate banner and print
ascii_banner = pyfiglet.figlet_format("Lyrics Generator")
print(ascii_banner)

# User selection Menu
print("Welcome to Lyrics Generator, select a genre of music you'd like to generate lyrics for: ")

# Print list of available genres
genres = ["Country", "Pop", "R&B", "Rap", "Rock", "Metal"]
for genre in genres:
    print(genre)
print("Type \"quit\" to exit.\n")

# Get user input
user_input = input("Genre: ")

# Make user input case insensitive
user_input = user_input.lower().strip()
genre_lookup = [x.lower() for x in genres]

# Generate lyrics, exit, or user-friendly error message when genre not found
while user_input != "quit":
    if user_input in genre_lookup:

        # Choosing genre text file
        lyrics = ""
        rel_paths = ["lyrics/countrylyrics.txt", "lyrics/poplyrics.txt", "lyrics/rblyrics.txt", "lyrics/raplyrics.txt", "lyrics/rocklyrics.txt", "lyrics/metallyrics.txt"]
        if user_input == "country":
            lyrics = rel_paths[0]
        elif user_input == "pop":
            lyrics = rel_paths[1]
        elif user_input == "r&b":
            lyrics = rel_paths[2]
        elif user_input == "rap":
            lyrics = rel_paths[3]
        elif user_input == "rock":
            lyrics = rel_paths[4]
        elif user_input == "metal":
            lyrics = rel_paths[5]

        # geniusclient.lyrics_scraper(user_input)
        print("\n")
        # os.system('python3 generate.py')
        words = generate.get_words_from_text(lyrics)
        g = generate.make_graph(words)
        composition = generate.compose(g, words, 100)
        print(' '.join(composition))
        print("\n")
        print("Select a genre of music you'd like to generate lyrics for or type \"quit\" to exit: ")
        for genre in genres:
            print(genre)
        user_input = input("\nGenre: ")
    else:
        user_input = input("Genre not found. Please choose a genre on the list: ")







