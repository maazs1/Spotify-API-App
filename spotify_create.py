import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username =sys.argv[1]
scope = 'playlist-read-private'
client_id ='bb2e3fbb3d464ce2b843bf5f2bfeebf0'
client_secret='645eef3583144fb3ae92f3985ea1a94b'
redirect_uri ='http://google.com/'
# User ID: mms532?si=KP6bNPqvRvi0hprG-vsJ3g

#set SPOTIPY_CLIENT_ID=bb2e3fbb3d464ce2b843bf5f2bfeebf0
#set SPOTIPY_CLIENT_SECRET=645eef3583144fb3ae92f3985ea1a94b
#set SPOTIPY_REDIRECT_URI=http://google.com/

#Erase cache and prompt for user persmission
try:
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

#Create spotifyObject
spotifyObject=spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']
follower = user['followers']['total']

while True:
    print()
    print(">>>Welcome to Spotipy " + displayName + "!")
    print(">>> You have " +str(follower) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - Exit")
    print()

    choice = input("Your choice: ")

    # Search for the artist
    if choice == "0": 
        print()
        searchQuery = input("What's the Artist Name?: ")
        print()

        # Get the search results
        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
        print(json.dumps(searchResults, sort_keys=True, indent=4))

        # Artist Details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0]) 
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        # Album Details
        trackURIs = []
        trackArt = []
        z = 0

        # Extract Album Data
        albumResults = spotifyObject.artist_albums(artistID)

    # Ends the program
    if choice =="1":
        break


# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
