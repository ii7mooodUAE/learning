import eyed3

audioFilePath = input("Audio file path? \n").replace('"','')
audiofile = eyed3.load(audioFilePath)

audiofile.tag.artist = input("Artist? \n")
audiofile.tag.album = input("Album? \n")
audiofile.tag.album_artist = input("Album Artist(s)? \n")
audiofile.tag.title = input("Title? \n")

path_to_artwork = input("Path to artwork? (jpg) \n")

try:
    with open(path_to_artwork, 'rb') as fp:
        artwork_data = fp.read()
    audiofile.tag.images.set(3, artwork_data, "image/jpeg", u"Description")

except Exception as e:
    print(e)
    input(" ")

audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
