from pymongo import MongoClient
import passw
password = passw.PASSWORD
cluster = "mongodb+srv://grovetender:"+password+"@faygrove.c0zaa.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)

# Miksi tämä pushaantuu eri tilillä ?

db = client['AlbumDB']
albums = db.Albums
col = db['Albums']

def fetch_albums():
    
    albumList = []
    for row in albums.find():
        albumList.append(f"{row['artist']}-{row['album']}-{row['year']}-{row['genre']}")
    return albumList

def remove(album):
    col.delete_one({'artist': album[0]})

def add_album(artist: str, album: str, year: int, genre: str):
    col.insert_one({'artist': artist, 'album': album, 'year': int(year), 'genre': genre})

def update(selectedAlbum, artist, album, year, genre):
    filterr = {
        'artist': selectedAlbum[0],
        'album': selectedAlbum[1],
        'year': int(selectedAlbum[2]),
        'genre': selectedAlbum[3]
    }
    newValues = {'$set':{
        'artist': artist,
        'album': album,
        'year': int(year),
        'genre': genre
    }}
    albums.update_one(filterr, newValues)

# Works for some odd reason ?
# def update(selectedAlbum, artist, album, year, genre):
#     selectedAlbum = {}
#     newValues = {'$set':{
#         'artist': artist,
#         'album': album,
#         'year': int(year),
#         'genre': genre
#     }}
#     albums.update_one(selectedAlbum, newValues)

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
