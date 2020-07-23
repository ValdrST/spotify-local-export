from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint
class SpotifyInterfaz(object):
    def __init__(self, client_id=None, client_secret=None):
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    
    def search_playlist(self, playlist_id=None):
        lista = []
        offset = 0
        while True:
            response = self.sp.playlist_tracks(playlist_id,fields='items.track', limit=100, offset=offset)
            lista.extend(response["items"])
            
            offset = offset + len(response['items'])
            if len(response["items"]) == 0:
                break
        playList = self.procesar_playlist(lista)
        return playList

    def procesar_playlist(self, playlist):
        lista_new = []
        for track in playlist:
            track_new = {"titulo":"",
                "artista":"",
                "album":""}
            track_new["titulo"] = track["track"]["name"]
            for artista in track["track"]["artists"]:
                track_new["artista"] = track_new["artista"] + artista["name"] + ","
            track_new["artista"] = track_new["artista"].split(",")
            track_new["album"] = track["track"]["album"]["name"]
            lista_new.append(track_new)
        return lista_new