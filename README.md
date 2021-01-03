# Automate-Apple-music
## Automatically add music that has been liked on youtube to spotify. 

I got the idea from this youtube video and decided to create my own version; https://www.youtube.com/watch?v=7J_qcttfnJA&ab_channel=TheComeUp


## To run the python script:
    python3 addmusic.py

## Process info with links and explanations
* After the script is run and if all the credentials have been set up correctly, a prompt with a link will appear on the command line to "Enter the authorization code:". Follow the link and instructions to get code (_Grant permission to View your YouTube account_). Enter the code and then wait for music to be added to playlist. A new code is needed for each run so the **old auth code would be expired** and useless.
* I retrieved **OAuth 2.0 Client IDs** and other credential info from https://console.developers.google.com/apis/. The Credentials section allows you to create credentials for your app and even download the credentials in a json format (_client_secret.json_) to be used by the youtube client in the code.
* AddMusic accesses youtube and gets all liked videos (via Youtube Data API). Sample requests to the API can be found here; https://developers.google.com/youtube/v3/docs (as well as embedded Python code to be used for API client connection). youtube_dl is used to get liked 'music' video info specifically (track and artist info) from all the liked videos retrieved from youtube.
* A playlist is created (via Spotify API), if it doesn't already exist. if it exists, the tracks will just be added to the existing playlist. The playlist id of the created or existing playlist and the uri values of the liked tracks are used when adding tracks to playlist. The uris of the tracks are retrieved from API search results of the track name and artist. The first song found (first uri in search result) is then added to spotify.
* Requests that can be sent to the API are found here, https://developer.spotify.com/console/. At the bottom of each page of requests, there is also a section that allows us to get auth tokens (OAuth Token). The spotify web api tokens only last for an hour, so new tokens are needed constantly. I selected all the __scopes__ in order to get a token that gave me full permissions to modify, but you might only need to select a few that deal with playlists modification. 
* The authtokens and userid info should be put in the secretinfo.py document so it can to be used by addmusic.py. userid is my spotify user Id and it can be found on the _Profile->Account_ section on https://www.spotify.com/.

* Playlist is named based on the date, e.g. **New Playlist Jan-03-2021**. 

## Sample run:
**python3 addmusic.py** <br>
Please visit this URL to authorize this application: "....." <br>
Enter the authorization code: "....." <br>
[youtube] LXXQLa-5n5w: Downloading webpage <br>
[youtube] hQsZUVMwEls: Downloading webpage <br>
[youtube] dXeOBkKdiAg: Downloading webpage <br>
... <br>
[youtube] pb29jzOCONY: Downloading webpage <br>
[youtube] Rv_QKcURXK0: Downloading webpage <br>
[youtube] VeFJlLStY-I: Downloading webpage <br>
**playlist already exists** <br>
**Adding song to playlist** <br>

#### Liked songs have been added to my Spotify to the _New Playlist Jan-03-2021_.