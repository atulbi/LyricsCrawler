import re
import urllib.request
from bs4 import BeautifulSoup
from raw import *

def parse(artist , song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    if artist.startswith("the"):    # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    return "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html"


def main():
    track = input("Enter the song name : ")
    artist = input("Enter artist name : ")
    details = getjson(track,artist)
    imglink = details[2]
    url = parse(details[1] ,details[0])
    content = urllib.request.urlopen(url).read()
    lyrics = find(content)
    print(lyrics)

def find(content):
    try: 
        soup = BeautifulSoup(content,'html.parser')
        lyrics = soup.body.find_all('b')[1].string +"\n"
        parent = soup.body.find_all('b')[1].parent
        i=0
        for tag in parent.children:
            if(tag.name=='div'):
                if i == 4:
                    for str in tag.strings:
                        lyrics= lyrics+str+'\n'
                i = i+1
        return lyrics
    except Exception as e:
        return "Exception Occured : "+'\n'+ str(e)+'\n'


if __name__=='__main__':
    main()