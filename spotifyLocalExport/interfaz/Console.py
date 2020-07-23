#!/usr/bin/env python
import argparse
import logging
import json
from pprint import pprint
from ..core import SpotifyInterfaz
from ..core import LocalFileInterfaz
from ..core import Buscador

class Console(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args = None
    
    def argumentParse(self):
        self.parser.add_argument("--cli", help="Modo consola",action="store_true",default=False)
        self.parser.add_argument("--dirs-input",help="Directorios de entrada", nargs="+",required=True, type=str)
        self.parser.add_argument("--playlist-id",help="id del playlist", nargs="?",required=True, type=str)
        self.parser.add_argument("--client-id",help="Client id de la api", nargs="?",required=True, type=str)
        self.parser.add_argument("--client-secret",help="Client secret de la api",required=True, nargs="?", type=str)
        self.parser.add_argument("--dir-out",help="Directorio de salida", required=True, nargs="?", type=str)
        self.parser.add_argument('--debug',default=True, action="store_true", help='modo debug')
        self.args = self.parser.parse_args()
    
    def iniciar(self):
        self.argumentParse()
        si = SpotifyInterfaz(client_id=self.args.client_id, client_secret=self.args.client_secret)
        spotify_track = si.search_playlist(self.args.playlist_id)
        lfi = LocalFileInterfaz(dirsInput=self.args.dirs_input, dirOutput=self.args.dir_out)
        lfi.procesarDirsInput()
        local_tracks = lfi.getLocalTracks()
        j = json.dumps(local_tracks)
        with open("local_tracks.json", "w") as f:
            f.write(j)
        j = json.dumps(spotify_track)
        with open("spotify_tracks.json", "w") as f:
            f.write(j)
        f_l = open("local_tracks.json","r")
        local_tracks = json.load(f_l)
        f_s = open("spotify_tracks.json","r")
        spotify_tracks = json.load(f_s)
        f_l.close()
        f_s.close()
        b = Buscador()
        no_encontrados = b.buscar(spotify_tracks, local_tracks)
        j = json.dumps(no_encontrados)
        with open("no_encontrados_tracks.json", "w") as f:
            f.write(j)
        paths = b.getListaPath()
        for path in paths:
            lfi.cpyArchivo(path)


