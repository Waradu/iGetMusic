import json
itunes = "https://itunes.apple.com/search?"

try:
    import requests
except ImportError as e:
    print(
        "\033[91m"+"== PLEASE INSTALL REQUESTS (pip install requests) =="+"\033[0m")


def getMultiple(term, country="GB", limit=50, explicit=True, entity="music"):
    apiUrl = f"{itunes}term={term}&entity={entity}&country={country}&limit={limit}&explicit={'Yes' if explicit else 'No'}"
    r = requests.get(apiUrl)

    data = r.json()

    return data


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


def resizeImage(url: str, size: int):
    url = url.replace("100x100bb.jpg", f"{size}x{size}bb.jpg")
    url = url.replace("60x60bb.jpg", f"{size}x{size}bb.jpg")
    url = url.replace("30x30bb.jpg", f"{size}x{size}bb.jpg")
    return url


"""
def getMinimalInfo(oldjson):
    minalList = []

    x = 0

    for item in oldjson["results"]:
        minalList.append([])
        minalList[x].append(item["trackName"])
        minalList[x].append(item["collectionName"])
        minalList[x].append(item["artistName"])
        minalList[x].append(item["artworkUrl100"])
        minalList[x].append(item["trackTimeMillis"])
        minalList[x].append(item["isStreamable"])
        minalList[x].append(False if item["trackExplicitness"]
                            == "notExplicit" else True)
        x += 1

    return minalList
"""


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

    def getArtist(self):
        return self.artistName

    def getCountry(self):
        return self.country
    
    def getTrackViewUrl(self):
        return self.trackViewUrl

    def Streamable(self):
        return self.isStreamable

    def getCollectionName(self):
        return self.collectionName

    def getResizedImage(self, size):
        return resizeImage(self.image, size)

    def ids(self, printList: bool = False):
        return [self.trackId, self.collectionId, self.artistId]

    def lenght(self):
        return self.trackTimeMillis

    def explicit(self):
        return self.trackExplicitness

    def searchForSongName(self, country="GB", limit=50, explicit=True):
        return getMultiple(self.trackName, country, limit, explicit, "song")

    def searchForArtist(self, country="GB", limit=50, explicit=True):
        return getMultiple(self.artistName, country, limit, explicit, "allArtist")

    def searchForCollectionName(self, country="GB", limit=50, explicit=True):
        return getMultiple(self.collectionName, country, limit, explicit, "album")


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
        return getMultiple(self.artistName, country, limit, explicit, "allArtist")


def get(term, country="GB", explicit=True):

    apiUrl = f"{itunes}term={term}&entity=song&country={country}&limit=1&explicit={'Yes' if explicit else 'No'}"
    r = requests.get(apiUrl)
    data = r.json()

    data = data["results"][0]

    songData = song(data)

    return songData

def getArtist(term, country="GB", explicit=True):

    apiUrl = f"{itunes}term={term}&entity=allArtist&country={country}&limit=1&explicit={'Yes' if explicit else 'No'}"
    r = requests.get(apiUrl)
    data = r.json()

    data = data["results"][0]

    songData = artist(data)

    return songData
