# 1. Log into youtube
# 2. get all liked music videos
# 3. create a new playlist
# 4. search for song
# 5. add to playlist

import requests
import datetime
import json
from secretinfo import userid,authtoken

class AddMusic():

    # init method or constructor


    def __init__(self):
       self.date = datetime.datetime.now();
       self.track = "hello"
       self.artist = "jorja"


    def access_youtube(self):
        pass

    def get_liked_music(self):
        pass
    
    #check if playlist name already exists
    def doesplaylistexist(self,name):
        url = 'https://api.spotify.com/v1/users/{}/playlists'.format(userid)
        response = requests.get(url, headers = {"Content-Type": "application/json", "Authorization":"Bearer {}".format(authtoken)})
        total=response.json()["total"]
        for i in range(0,int(total)):
            if response.json()["items"][i]["name"] == name:
                a= True
                self.playlistid = response.json()["items"][i]["id"]
                break
            else:
                a= False
        return a
    
    #create new playlist or get existing playlist id
    #generates playlist name by date e.g. New Playlist Jan-02-2021
    def create_playlist(self):
        
        playlistname = "New Playlist "+str(date.strftime("%B")[0:3])+"-"+str(date.strftime("%d"))+"-"+str(date.year)
        if able.doesplaylistexist(playlistname):
            playlistid = able.playlistid
            print("playlist already exists ")
            #print("playlist id: "+str(able.playlistid))
        else:
            url = 'https://api.spotify.com/v1/users/{}/playlists'.format(userid)
            obj = json.dumps({"name": playlistname,
            "description": "New playlist description",
            "public": "false"})
            print("playlist does not exist, creating new playlist")
            response = requests.post(url, data = obj, headers = {"Content-Type": "application/json", "Authorization":"Bearer {}".format(authtoken)})
            playlistid = response.json()["id"]
            #print("new playlist id: "+str(playlistid))
        
        return playlistid
        



    def search_add(self,track):
        
        url = 'https://api.spotify.com/v1/search?q={}&type=track&market=US&limit=20&offset=0'.format(track)
        response = requests.get(url, headers = {"Content-Type": "application/json", "Authorization":"Bearer {}".format(authtoken)})
        print(url)
        uri = response.json()["tracks"]["items"][0]["uri"] #just first song
        print(uri)
        
able = AddMusic()
date = able.date
able.search_add(able.track)
able.create_playlist()
