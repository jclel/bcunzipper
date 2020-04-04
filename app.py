from zipfile import ZipFile 
import os
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

filenames = input()

# Handling multipe zip files
list_of_files = filenames.split('"')
files_to_unzip = []
# Remove blank items from list
for zips in list_of_files:
    if zips is not '':
        files_to_unzip.append(zips)

# Set the root dir to wherever this is run from.
root_dir = os.getcwd()

def unzip(file):
    # Set where we're going to unzip the files to
    # Which is whatever is returned after artist/album folders are created
    zip_destination = createFolders(file)
    # Make sure we're in the same directory as the program and the zip files.
    os.chdir(root_dir)
    # If we've actually created folders, we can unzip them.
    # If createFolders() returned 0, we didn't make new folders, so we skip it altogether.
    # And you can reflect on how better to keep track of what songs you already have ;)
    if zip_destination is not 0:
        print("Unzipping zip file from " + root_dir)
        with ZipFile(file, 'r') as zip:
            # Change to newly created folders
            os.chdir(zip_destination)
            print("And unzipping file to " + zip_destination)
            # Unzip contents into there
            print("Extracting...")
            zip.extractall()

    # Return to root folder to do it all again for the next zip file.
    os.chdir(root_dir)


def getArtistAndAlbumName(file):
    # Get the artist and album name by splitting the filename by the '-'
    array = file.split(" - ")
    return array
    

def checkFolders(file):
    # Make a list of all the folders in the root directory.
    root_folders = os.listdir(os.getcwd())
    # Retrieve artist and album name by splitting zip file name.
    array = getArtistAndAlbumName(file)
    artist_name = array[0]
    album_name = array[1]
    # Remove .zip from folder name with a substring
    album_name = album_name[:-4]

    dir_to_create = ""
    
    for root_folder in root_folders:
        # If the artist already exists
        if root_folder in artist_name:
            # Check for contents of artist folder.
            os.chdir(artist_name)
            print(f"Checking folder in {os.getcwd()}")

            # If there aren't any folders in the artist folder
            # Pass album name as the folder to create
            if not os.listdir(os.getcwd()):
                dir_to_create = album_name
            else:
                # If the album already exists, we won't make the folder again.
                for albums in os.listdir(os.getcwd()):
                    if albums in album_name:
                        # Don't create any new folders
                        dir_to_create = 0
                        return dir_to_create
                    # If other albums exist but not this one
                    # Pass current album as the folder to create
                    # And return to root directory.
                    else:
                        print("Making album name folder " + album_name )
                        dir_to_create = album_name
                        os.chdir(root_dir)
        # If the artist doesn't exist, pass artists and album folders to be created.
        else:
            dir_to_create = artist_name + "/" + album_name + "/"

    return dir_to_create

def createFolders(file):
 
    dir_to_create = checkFolders(file)
    os.chdir(root_dir)
    
    if dir_to_create is 0:
        print("Found! Skipping...")
        return 0
    else:
        # Create whatever folders were returned from checkFolders()
        os.makedirs(dir_to_create)
        print(f"Made folder in {os.getcwd()}: {dir_to_create}")
    # Change directory to the folder we just created.
    os.chdir(dir_to_create)
    # And pass that folder back to the calling method.
    dir_to_unzip_to = os.getcwd()
    return dir_to_unzip_to

for file in files_to_unzip:
    # For every zip file passed to the program, unzip and organise.
    # And pray it doesn't break.
    unzip(file)