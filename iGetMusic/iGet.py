import json
itunes = "https://itunes.apple.com/search?"
itunesLoockUp = "https://itunes.apple.com/lookup?"

try:
    import requests
except ImportError as e:
    print(
        "\033[91m"+"== PLEASE INSTALL REQUESTS (pip install requests) =="+"\033[0m")
    raise SystemExit


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class song:
    def __init__(self, json):

        if "results" in json:
            try:
                json = json["results"][0]
            except:
                pass

        self.kind = json["kind"]
        self.artistName = json["artistName"]
        self.collectionName = json["collectionName"]
        self.trackName = json["trackName"]
        self.artistViewUrl = json["artistViewUrl"]
        self.collectionViewUrl = json["collectionViewUrl"]
        self.trackViewUrl = json["trackViewUrl"]
        self.image = json["artworkUrl100"]
        self.releaseDate = json["releaseDate"]
        self.collectionExplicitness = False if json["collectionExplicitness"] == "notExplicit" else True
        self.trackExplicitness = False if json["trackExplicitness"] == "notExplicit" else True
        self.discCount = json["discCount"]
        self.discNumber = json["discNumber"]
        self.trackCount = json["trackCount"]
        self.trackTimeMillis = json["trackTimeMillis"]
        self.country = json["country"]
        self.primaryGenreName = json["primaryGenreName"]
        self.isStreamable = str(json["isStreamable"])
        self.artistId = json["artistId"]
        self.collectionId = json["collectionId"]
        self.trackId = json["trackId"]

    def getImage(self):
        return self.image

    def getName(self):
        return self.trackName

    def getArtistName(self):
        return self.artistName

    def getCountry(self):
        return self.country

    def getTrackViweUrl(self):
        return self.trackViewUrl

    def sreamable(self):
        return self.isStreamable

    def getCollectionName(self):
        return self.collectionName

    def getResizedImage(self, size):
        return resizeImage(self.image, size)

    def ids(self):
        return [self.trackId, self.collectionId, self.artistId]

    def lenght(self):
        return self.trackTimeMillis

    def explicit(self):
        return self.trackExplicitness

    def searchForSongName(self, country="GB", limit=50, explicit=True):
        return get(self.trackName, country, limit, explicit)

    def searchForArtist(self, country="GB", limit=50, explicit=True):
        return getArtist(self.artistName, country, limit, explicit)


class artist:
    def __init__(self, json):

        if "results" in json:
            try:
                json = json["results"][0]
            except:
                pass

        self.wrapperType = json["wrapperType"]
        self.artistType = json["artistType"]
        self.artistName = json["artistName"]
        self.artistLinkUrl = json["artistLinkUrl"]
        self.primaryGenreName = json["primaryGenreName"]
        self.primaryGenreId = json["primaryGenreId"]
        self.artistId = json["artistId"]

    def getName(self):
        return self.artistName

    def getArtistLinkUrl(self):
        return self.artistLinkUrl

    def getArtistID(self):
        return self.artistId

    def getType(self):
        return self.artistType

    def getGenre(self):
        return [self.primaryGenreName, self.primaryGenreId]

    def searchForArtist(self, country="GB", limit=50, explicit=True):
        return getArtist(self.artistName, country, limit, explicit)

    def getAllArtistSongs(self):
        return getArtistSongs(self.artistId)


def resizeImage(url, size):
    url = url.replace("100x100bb.jpg", f"{size}x{size}bb.jpg")
    url = url.replace("60x60bb.jpg", f"{size}x{size}bb.jpg")
    url = url.replace("30x30bb.jpg", f"{size}x{size}bb.jpg")
    return url


def get(term, country="GB", limit=50, explicit=True):

    apiUrl = f"{itunes}term={term}&entity=song&country={country}&limit={limit}&explicit={'Yes' if explicit else 'No'}"
    r = requests.get(apiUrl)
    data = r.json()

    data = data["results"]

    songList = []

    for item in data:
        songList.append(song(item))

    return songList


def getArtist(term, country="GB", explicit=True):

    apiUrl = f"{itunes}term={term}&entity=allArtist&country={country}&limit=1&explicit={'Yes' if explicit else 'No'}"
    r = requests.get(apiUrl)
    data = r.json()

    data = data["results"]

    songList = []

    for item in data:
        songList.append(artist(item))

    return songList


def getAllArtistSongs(id):

    apiUrl = f"{itunesLoockUp}id={id}&entity=song"
    r = requests.get(apiUrl)
    data = r.json()

    data = data["results"]

    songList = []

    artistData = artist(data[0])

    del data[0]
    for item in data:
        songList.append(song(item))

    return songList, artistData
