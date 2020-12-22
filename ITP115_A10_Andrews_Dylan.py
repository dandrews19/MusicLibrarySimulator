# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Assignment 10
# Description:
# This program will simulate a user's music library using an already-created music library, and save the music library
# with any changes back in the same file

import MusicLibraryHelper
import random

# displays menu with all the options for the music platform
def displayMenu():
    print("Welcome to Your Music Library\nOptions:\n\t1) Display Library\n\t2) Display all artists\n\t3) Add an album"
          "\n\t4) Delete an album\n\t5) Delete an artist\n\t6) Search library\n\t7) Generate a random playlist\n\t8) Exit")

# allows user to display library, lists all artists and their albums
def displayLibrary(musicLibDictionary):
    artists = list(musicLibDictionary.keys())
    albumsList = list(musicLibDictionary.values())
    i = 0
    while i < len(artists):
        print("Artist:", artists[i])
        c = 0
        print("Albums:")
        artistAlbumList = list(albumsList[i])
        while c < len(artistAlbumList):
            print("\t -", artistAlbumList[c])
            c += 1
        i += 1
    print("\n")

# displays all artists in library
def displayArtists(musicLibDictionary):
    print("Displaying all artists:")
    artists = list(musicLibDictionary.keys())
    i = 0
    while i < len(artists):
        print("-", artists[i])
        i += 1

# allows user to add an album to an existing artist
def addAlbum(musicLibDictionary):
    artists = list(musicLibDictionary)
    artist = input("Enter artist: ")
    artist = artist.strip().lower().title()
    while artist not in artists:
        artist = input("Enter artist in library: ")
        artist = artist.strip().lower().title()
    album = input("Enter album: ")
    album = album.lower().title().strip()
    musicLibDictionary[artist] = album

# allows user to delete an album in library, returns true or false based on whether it was able to delete something
def deleteAlbum(musicLibDictionary):
    artists = list(musicLibDictionary.keys())
    artistDelete = input("Enter artist: ")
    artistDelete = artistDelete.lower().title().strip()
    while artistDelete not in artists:
        artistDelete = input("Enter artist in library: ")
        artistDelete = artistDelete.lower().title().strip()
    albumDelete = input("Enter album: ")
    albumDelete = albumDelete.lower().title().strip()
    albumList = musicLibDictionary.get(artistDelete)
    if albumDelete not in albumList:
        return False
    else:
        albumList.remove(albumDelete)
        musicLibDictionary[artistDelete] = albumList
        return True



# allows user to delete an artist in library and all of their albums, returns true or false based on if it was able to
# delete something
def deleteArtist(musicLibDictionary):
    artists = list(musicLibDictionary.keys())
    artistDelete = input("Enter artist: ")
    artistDelete = artistDelete.strip().lower().title()
    if artistDelete not in artists:
        return False
    else:
        del musicLibDictionary[artistDelete]
        return True


# allows user to search library for key words and display albums and artists containing the word / phrase
def searchLibrary(musicLibDictionary):
    searchOriginal = input("Please enter a search term: ")
    artists = list(musicLibDictionary.keys())
    albums = list(musicLibDictionary.values())
    search = searchOriginal.strip().lower().title()
    print("Artists containing '" + searchOriginal + "'")
    i = 0
    resultsArtists = False
    while i < len(artists):
        if search in artists[i]:
            print("- " + artists[i])
            resultsArtists = True
        i += 1
    if resultsArtists == False:
        print("\tNo results")
    print("Albums containing '" + searchOriginal + "'")
    c = 0
    resultsAlbums = False
    while c < len(albums):
        artistAlbumList = list(albums[c])
        h = 0
        while h < len(artistAlbumList):
            if search in artistAlbumList[h]:
                print("-", artistAlbumList[h])
                resultsAlbums = True
            h += 1
        c += 1
    if resultsAlbums == False:
        print("\tNo results")

# generates a random playlist of the artists and albums
def generateRandomPlaylist(musicLibDictionary):
    artists = list(musicLibDictionary.keys())
    editArtists = list(musicLibDictionary.keys())
    albums = list(musicLibDictionary.values())
    i = 0
    print("Here is your random playlist:")
    while i < len(artists):
        number = random.randrange(0, len(editArtists))
        num2 = random.randrange(0, len(albums[number]))
        artistAlbumList = list(albums[number])
        print("-", artistAlbumList[num2], "by", editArtists[number])
        editArtists.pop(number)
        albums.pop(number)
        i += 1

# runs the library program until user enters 8 and saves it after they press 8
def main():
    library = MusicLibraryHelper.loadLibrary("musicLibrary.dat")
    print(library)
    choice = 0
    while int(choice) != 8:
        displayMenu()
        choice = input("> ")
        while (choice.isdigit() == False) or (int(choice) not in range(1, 9)):
            choice = input("Make a proper selection (1-8): ")
        if int(choice) == 1:
            displayLibrary(library)
        elif int(choice) == 2:
            displayArtists(library)
        elif int(choice) == 3:
            addAlbum(library)
        elif int(choice) == 4:
            delete = deleteAlbum(library)
            if delete == True:
                print("Delete album success!")
            elif delete == False:
                print("Delete album failed.")
        elif int(choice) == 5:
            artistDelete = deleteArtist(library)
            if artistDelete == True:
                print("Delete artist success!")
            elif artistDelete == False:
                print("Delete artist failed.")
        elif int(choice) == 6:
            searchLibrary(library)
        elif int(choice) == 7:
            generateRandomPlaylist(library)
    print("Saving music library...")
    MusicLibraryHelper.saveLibrary("musicLibrary.dat", library)
    print("Goodbye!")







main()

