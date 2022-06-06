from pymongo import MongoClient
import passw
password = passw.PASSWORD
cluster = "mongodb+srv://grovetender:"+password+"@faygrove.c0zaa.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)

def fetch_albums():
    db = client['AlbumDB']
    albums = db.Albums
    albumList = []
    for row in albums.find():
        albumList.append(f"{row['artist']}-{row['album']}-{row['year']}-{row['genre']}")
    return albumList

def remove(album):
    db = client['AlbumDB']
    col = db['Albums']
    col.delete_one({'artist': album[0]})

def add_album(artist: str, album: str, year: int, genre: str):
    db = client['AlbumDB']
    col = db['Albums']
    col.insert_one({'artist': artist, 'album': album, 'year': int(year), 'genre': genre})

# Toimii myös vaihtoehtoisena syntaksina
# db = client['AlbumDB]
# db = client.AlbumDB
# albums = db.Albums

# Tulostetaan tietokannan collectioneiden nimet
# print(db.list_collection_names())

# Hakee kaikki tietueet
# result = albums.find()
# for row in result:
# Jokaisen rivin artist- ja album-avaimien arvot 
#    print(row['artist'],row['album'])

# Yhden tietueen haku
# print(albums.find_one())

# Yhden tietyn kentän mukaan
# print(albums.find_one({'album': 'The Kick Inside'}))
