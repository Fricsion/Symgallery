import os

def addToAlbum(items, specified_album): # items: list of items that are supposed to added to the album
    os.system("mkdir "+specified_album)
    for item in items:
        os.system("mv "+item+" "+specified_album+"/"+"item")
    return 1

def getAlbums(initials):
    os.system("ls "+initials+"*")



