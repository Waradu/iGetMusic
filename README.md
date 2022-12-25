# iGetMusic
Python iGetMusic API used to get music Name, Artist, ImageURL usw. <br>
See project on [pypi.org](https://pypi.org/project/iGetMusic/)

## Introduction
Use `pip install iGetMusic` to install the package.<br>
After that install requests `pip install requests`<br>

Import package with `import iGetMusic as iGet`

### Get song by name:

```py
iGet.get(term=songName)
```
You will get a json with the top 50 results. To change how many results you want to get with `limit=int` <br>
Set from which country you want to get results with `country="CountryCode"` (Default "GB"). <br>
See all codes at [Wikipedia](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements). <br>
Toggle explicit content with `explicit=True/False`.

### Get minimal info:
```py
iGet.getMinimalInfo(iGet.get(term=songName))
```
All songs will be converted into a list with a list per song in it.<br>
`results[SongNumber][0]` =  trachkName: Str <br>
`results[SongNumber][1]` =  artistName: Str <br>
`results[SongNumber][2]` =  artworkUrl100 (100x100): Str (imageURL) <br>

### Resize image with URL:
```py
iGet.resizeImage(siGet.getMinimalInfo(iGet.get(term=songName))[0][2], size)
```
This resizes the image by changing the imageURL.
