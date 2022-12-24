itunes = "https://itunes.apple.com/search?"
import requests
import json

def get(term, country = "GB", limit = 50, explicit = True):
  apiUrl = f"{itunes}term={term}&entity=song&country={country}&limit={limit}&explicit={'Yes' if explicit else 'No'}";
  r = requests.get(apiUrl)
  
  data = r.json()
  
  return data

def resizeImage(url: str, size: int):
  url = url.replace("100x100bb.jpg", f"{size}x{size}bb.jpg")
  url = url.replace("60x60bb.jpg", f"{size}x{size}bb.jpg")
  url = url.replace("30x30bb.jpg", f"{size}x{size}bb.jpg")
  return url

def getMinimalInfo(oldjson):
  minalList = []
  
  x = 0
  
  for item in oldjson["results"]:
    minalList.append([])
    minalList[x].append(item["trackName"])
    minalList[x].append(item["artistName"])
    minalList[x].append(item["artworkUrl100"])
    x += 1
    
  return minalList