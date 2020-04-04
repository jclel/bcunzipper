import os

cwd = os.getcwd()
print(cwd)
print(os.listdir(cwd))
artist_name = "Simo Soo"
album_name = "Pink Metal"
test_name = "Test"
# os.chdir()
# print(os.getcwd())
# print(os.listdir(os.getcwd()))

def checkFolders(artist_name, album_name):
    if artist_name in os.listdir(os.getcwd()):
        os.chdir(artist_name + "/")

        if album_name in os.listdir(os.getcwd()):
            os.chdir(album_name + "/")
            os.makedirs(test_name)
            print("Found album name and made test folder")
        else:
            os.makedirs(album_name)
            print("Found artist name and made album folder")
    else:
        print(artist_name)
        print(os.listdir(os.getcwd()))
        os.makedirs(artist_name + "/" + album_name)

checkFolders(artist_name, album_name)