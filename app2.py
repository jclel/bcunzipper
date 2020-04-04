from zipfile import ZipFile 
import os
import glob

filenames = ["Simo Soo - Pink Metal.zip", "Simo Soo - Pink Metsal2.zip", "Simon Soon - Pink Metal3.zip"]


# Function to check which folders exist and RETURN a string with the directory names to be made
# Function to create the folders
# Function to unzip (open zip file, then chdir to album folder, extractall)
# All wrapped in a for loop that traverses the filenames list

# CURRENT ISSUES
# Creating all new folders: GOOD
# Creating new subdirs if other albums already exist in artist folder: GOOD
# Creating new subdirs if NO albums already in artist folder: not good

root_dir = os.getcwd()

def unzip(file):
    # createFolders()
    # do the zipfile thing
    zip_destination = createFolders(file)
    os.chdir(root_dir)
    if zip_destination is not 0:
        print("Unzipping zip file from " + root_dir)
        with ZipFile(file, 'r') as zip:
            # Change to newly created folders
            os.chdir(zip_destination)
            print("And unzipping file to " + zip_destination)
            # Unzip contents into there
            print("Extracting...")
            zip.extractall()
    else:
        pass
    os.chdir(root_dir)


def getArtistAndAlbumName(file):
    # Get the artist and album name by splitting the filename by the '-'
    array = file.split(" - ")
    return array
    

def checkFolders(file):
    root_folders = os.listdir(os.getcwd())

    array = getArtistAndAlbumName(file)
    artist_name = array[0]
    album_name = array[1]
    # Remove .zip from folder name with a substring
    album_name = album_name[:-4]

    dir_to_create = ""
    
    for root_folder in root_folders:
        # if artist and album exists
        #print("Root folder found " + root_folder)
        if root_folder in artist_name:
            print("Artist name found, it's " + artist_name)
            os.chdir(artist_name)
            print("Checking folder in " + os.getcwd())
            for albums in os.listdir(os.getcwd()):
                if albums in album_name:
                    print("Album: " + albums + " ALbum name: " + album_name)
                    dir_to_create = 0
                    return dir_to_create
                else:
                    print("Making album name folder " + album_name )
                    dir_to_create = album_name
                    os.chdir(root_dir)
        else:
            dir_to_create = artist_name + "/" + album_name + "/"
    # root_folders = listdir(root dir)
    # if artist_name exists in root_folders, and album_name exists in artist_name, return "found"
    # if artist_name exists and album_name not found, return artist_name/album_name
    # if artist name doesn't exist, return artist_name)
    return dir_to_create

def createFolders(file):
    # if checkFolders() is "found", print("Found! Skipping...")
    # else makedir(checkFolders())
    print("Creating folder in " + os.getcwd())
    dir_to_create = checkFolders(file)
    #print("Dir to create: " + dir_to_create)
    if dir_to_create is 0:
        print("Found! Skipping...")
        return 0
    else:
        os.makedirs(dir_to_create)
        print("Made folder in " + os.getcwd() + ": " + dir_to_create)
    os.chdir(dir_to_create)
    dir_to_unzip_to = os.getcwd()
    return dir_to_unzip_to

for file in filenames:
    # createFolders(file)
    unzip(file)