from zipfile import ZipFile 
import os
from pathlib import Path
import shutil
import glob

print("****************************************************")
print("****************************************************")
print( "______  ___  _   _______  _____  ___ ___  ________ ")
print( "| ___ \/ _ \| \ | |  _  \/  __ \/ _ \|  \/  | ___ \"")
print( "| |_/ / /_\ \  \| | | | || /  \/ /_\ \ .  . | |_/ /")
print( "| ___ \  _  | . \` | | | || |   |  _  | |\/| |  __/ ")
print( "| |_/ / | | | |\  | |/ / | \__/\ | | | |  | | |    ")
print( "\____/\_| |_|_|_\_/___/___\____|_|_|_|_|__|_|_|__  ")
print( "| | | | \ | ||___  /_   _| ___ \ ___ \  ___| ___ \ ")
print( "| | | |  \| |   / /  | | | |_/ / |_/ / |__ | |_/ / ")
print( "| | | | . \` |  / /   | | |  __/|  __/|  __||    /  ")
print( "| |_| | |\  |./ /____| |_| |   | |   | |___| |\ \  ")
print( " \___/\_| \_/\_____/\___/\_|   \_|   \____/\_| \_| ")
print( "                                                   ")
print("                    by jakec                        ")
print("****************************************************")
print("****************************************************")

print( "                                                   ")

print("Drag the zip files onto this window and press enter")

file_name = input()

# Handling multipe zip files
list_of_files = file_name.split('"')
files_to_unzip = []
# Remove blank items from list
for zips in list_of_files:
    if zips is not '':
        files_to_unzip.append(zips)
    

def unzip(file_name):
    # Get the root directory to start every time this is run
    # After traversing directories later, we can use this variable to return to where all our zips are
    root_dir = os.getcwd()

    # Get the artist and album name by splitting the filename by the '-'
    array = file_name.split(" - ")
    artist_name = array[0]
    album_name = array[1]
    # Remove .zip from folder name with a substring
    album_name = album_name[:-4]
    # Make a list of folders in the current directory
    list_of_existing_folders = os.listdir(root_dir)
    for folder in list_of_existing_folders:
        # If a folder for the artist already exists
        if folder is artist_name:
            # Change to the artist folder
            os.chdir(artist_name)
            # And only create an album name folder
            dirname = album_name + "/"
        else:
            # Create artist and album folders
            dirname = artist_name + "/" + album_name + "/"
   
    # Create the directory and subdirectory
    os.makedirs(dirname)

    with ZipFile(file_name, 'r') as zip:
        # Change to newly created folders
        os.chdir(dirname)
        # Unzip contents into there
        print("Extracting...")
        zip.extractall()
        
    # Create a list of newly unzipped songs
    # We use glob to pattern match the filenames so we don't accidentally rename cover images etc
    songs = []
    # Only get mp3s
    for file in glob.glob("*.mp3"):
        songs.append(file)

    for song in songs:
        # Remove all the stuff in the filename before the '-' (e.g. artist name)
        song_title = song.split(" - ")
        # Tell the system the actual song title is the part that comes AFTER the '-'
        song_title = song_title[-1]
        # Print changes being made to the console
        print(f"Changing {song} -> {song_title}")
        # Rename the songs
        os.rename(song, song_title)
    # Change back to our original directory, ready to unzip some more songs
    os.chdir(root_dir)

for file in files_to_unzip:
    # Create another array with the constituent parts of the absolute path
    filepath_parts = file.split("\\")
    # Just get the last part (the actual filename w/o dir names)
    actual_filename = filepath_parts[-1]
    # Run the unzip function
    unzip(actual_filename)

print("\nFinished! Press enter to quit.")
endtime = input()