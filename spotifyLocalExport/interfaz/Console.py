#!/usr/bin/env python
import argparse
import logging
import json
from pprint import pprint
from ..core import SpotifyInterfaz
from ..core import LocalFileInterfaz

class Console(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args = None
    
    def argumentParse(self):
        self.parser.add_argument("--cli", help="Modo consola",action="store_true",default=False)
        self.parser.add_argument("--dirs-input",help="Directorios de entrada", nargs="+", type=str)
        self.parser.add_argument("--playlist-id",help="id del playlist", nargs="?", type=str)
        self.parser.add_argument("--client-id",help="Client id de la api", nargs="?", type=str)
        self.parser.add_argument("--client-secret",help="Client secret de la api", nargs="?", type=str)
        self.parser.add_argument("--dir-out",help="Directorio de salida", nargs="?", type=str)
        self.parser.add_argument('--debug',default=True, action="store_true", help='modo debug')
        self.args = self.parser.parse_args()
    
    def iniciar(self):
        self.argumentParse()
        #si = SpotifyInterfaz(client_id=self.args.client_id, client_secret=self.args.client_secret)
        #r = si.search_playlist(self.args.playlist_id)
        lfi = LocalFileInterfaz(dirsInput=self.args.dirs_input)
        lfi.procesarDirsInput()
        local_tracks = lfi.getLocalTracks()
        j = json.dumps(local_tracks)
        with open("local_tracks.json", "w") as f:
            f.write(j)
