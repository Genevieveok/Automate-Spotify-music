# 1. Log into youtube
# 2. get all liked music videos
# 3. log into apple music
# 4. create a new playlist
# 5. search for song
# 6. add to playlist
import requests
from secretinfo import userid
from secretinfo import authtoken
class AddMusic():

    # init method or constructor


    def __init__(self):
       pass


    def access_youtube(self):
        pass

    def get_liked_music(self):
        pass
    
    
    def access_apple_music(self):
        print(authtoken)
        #response = requests.get("https://api.spotify.com/v1/users/12160778651/playlists" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQBI3nsOXxRRt-8_n7sQzysl1opN9xIIJ1VdUgyuJlAEf7xUgAZI8a_ssOlEFNRcDQTMu7HlKIxix_1dLAPtF6nIR0HSLoTpVGaGQRG44z4nZZK4Kd6UmsJroqfGrxIQhFiZfcnn8zpRX0GKamjeilL8ArKJWuyFmP6VfBYD5t2hIisPlkegWrE56_iqhybO2Oj0OqIBfvVfgcnLWsXA3Pjgq7b_z6J2Tf7sdw")
        
        #print(response.status_code)
        


    def create_playlist(self):
        pass

    def search_add(self):
        pass
able = AddMusic()
able.access_apple_music()