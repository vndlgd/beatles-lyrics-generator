# Library to access content on Genius.com
import lyricsgenius as lg

# Search and manipulate strings
import re

# We retrieve data from the Genius API using the LyricsGenius python module
api = lg.Genius("my_access_token_here",
		skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

# Write to file
file = open("lyrics.txt", "w")

# Getting lyrics of songs by genre
page = 1
count = 0 
while page <= 2:
# Try Except statements to handle when a timeout occurs
    try:
        results = api.tag('country', page=page)
        for hit in results['hits']:
            song_lyrics = api.lyrics(song_url=hit['url'], )
            file.write(song_lyrics)
        page = results['next_page']      
    except:
        pass

file.close()


