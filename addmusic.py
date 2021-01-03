# 1. Log into youtube
# 2. get all liked music videos
# 3. create a new playlist
# 4. search for song
# 5. add to playlist

import requests
import datetime
import json
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from secretinfo import userid,authtoken
import youtube_dl

class AddMusic():

    #init method or constructor
    def __init__(self):
       self.date = datetime.datetime.now();
       self.dict_uris ={}
       
       


    def access_youtube(self):
        #get youtiube client
        #copying code from youtube data api
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        #json file with credential info for access to youtube data api
        client_secrets_file = "client_secret.json"
        scopes =["https://www.googleapis.com/auth/youtube.readonly"]

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
        #print(youtube)
        return youtube

        

    def get_liked_music(self):

        request = self.access_youtube().videos().list( 
            part="snippet,contentDetails,statistics",
            maxResults=25,
            myRating="like")
        
        response = request.execute()
        newresponse = json.dumps(response)
        #print(newresponse)

        #info for youtube video
        for i in response["items"]:
            video_title = i["snippet"]["title"]
            youtubes = "https://www.youtube.com/watch?v={}".format(i["id"])

            # collect track info and artist info to be used later
            video = youtube_dl.YoutubeDL({}).extract_info(youtubes, download=False)
            track = video["track"]
            artist = video["artist"]

            if track is not None and artist is not None:
                self.dict_uris[video_title] = {
                    "track": track,
                    "artist": artist,
                    "uris": self.get_uri(track, artist)}
    
    #check if playlist name already exists
    def doesplaylistexist(self,name):
        url = 'https://api.spotify.com/v1/users/{}/playlists'.format(userid)
        response = requests.get(url, headers = {"Content-Type": "application/json", "Authorization":"Bearer {}".format(authtoken)})
        #total playlists
        total=response.json()["total"]
        for i in range(0,int(total)):
            #compare name to all names of playlist that exist
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
        date = self.date;
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
        
    def get_uri(self,track,artist):
        #search for track and get uri for first one found (likely the track)
        #url = 'https://api.spotify.com/v1/search?q={}&type=track&market=US&limit=20&offset=0'.format(track)
        
        url = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(track,artist)
        response = requests.get(url, headers = {"Content-Type": "application/json", "Authorization":"Bearer {}".format(authtoken)})
        #print(url)
        uri = response.json()["tracks"]["items"][0]["uri"] #just first song
        return uri

    def add_songs(self):

        #retrieve all liked videos 
        self.get_liked_music()
        uris=[]

        #create list with uris for all videos
        for i,j in self.dict_uris.items():
            uris.append(j["uris"])

        datas = json.dumps(uris)
        #print(datas)
        #get new or existing playlist id and add searched track uri to playlist
        playid = self.create_playlist()
        url = '	https://api.spotify.com/v1/playlists/{}/tracks'.format(playid)
        #obj = json.dumps({"uris": uri})
        obj = datas
        print("Adding song to playlist")
        response = requests.post(url, data = obj, headers = {"Content-Type": "application/json", "Authorization":"Bearer {}".format(authtoken)})
        
able = AddMusic()
able.add_songs()

