from pymongo import MongoClient
import passw
password = passw.PASSWORD
cluster = "mongodb+srv://grovetender:"+password+"@faygrove.c0zaa.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)

class Database:
    def __init__(self):
        db = client['AlbumDB']
        self.albums = db.Albums
        self.col = db['Albums']

    def fetch_albums(self):
        
        albumList = []
        for row in self.albums.find():
            albumList.append(f"{row['artist']}-{row['album']}-{row['year']}-{row['genre']}")
        return albumList

    def remove(self, album):
        self.col.delete_one({'artist': album[0]})

    def add_album(self, artist: str, album: str, year: int, genre: str):
        self.col.insert_one({'artist': artist, 'album': album, 'year': int(year), 'genre': genre})

    def update(self, selectedAlbum, artist, album, year, genre):
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
        self.albums.update_one(filterr, newValues)

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
