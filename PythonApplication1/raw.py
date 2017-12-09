import json
import urllib.request


#for guessing correct artist and track name and returning the meta data from 
def getjson(title,artist_name):
    artist = artist_name
    track = title
    YOUR_API_KEY= "9cfa2cee18f204c68b67fe0a4ce3b383"
    try:
        url= "http://ws.audioscrobbler.com/2.0/?method=track.search&track="+track+"&artist="+artist+"&limit=9&api_key="+YOUR_API_KEY+"&format=json"
        #print(url)
        json_r = urllib.request.urlopen(url).read()
        d = json.loads(json_r)
        with open('recived.json',"w") as out:
            json.dump(d,out)
        t= len(d["results"]["trackmatches"]["track"][0]["image"])
        #print(t)
        return d["results"]["trackmatches"]["track"][0]["name"],d["results"]["trackmatches"]["track"][0]["artist"],d["results"]["trackmatches"]["track"][0]["image"][t-1]["#text"]
    except :
        return "EXCEPTION RAISED"
