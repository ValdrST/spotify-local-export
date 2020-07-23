import pathlib
import hashlib
import shutil
import threading
import os
import logging
from pprint import pprint
from mutagen.easyid3 import EasyID3

class LocalFileInterfaz(object):
    def __init__(self, dirsInput=[], dirOutput=None):
        self.dirsInput = dirsInput
        self.dirOutput = dirOutput
        self.tipos = [".mp3", ".flac", ".aac", ".ogg", ".m4a"]
        self.localTracks = []
        self.templateTrack = {"titulo":"",
                "artista":"",
                "album":"",
                "path":""}
    
    def procesarDirsInput(self):
        self.localTracks = []
        for directorio in self.dirsInput:
            self.getPath(directorio = directorio)

    def getPath(self,directorio):
        lista = []
        for root, dirs, files in os.walk(directorio):
            for filename in files:
                t = threading.Thread(target=self.getDatos,args=(os.path.join(root, filename),lista,))
                t.start()
                t.join()
        self.localTracks.extend(lista)

    def getDatos(self, filename, lista):
        ext = pathlib.PurePosixPath(filename).suffix.lower()
        l = {"titulo":"",
                "artista":"",
                "album":"",
                "path":""}
        if ext in self.tipos:
            try:
                tag = EasyID3(filename)
                l["titulo"] = tag["title"][0]
                l["artista"] = tag["artist"]
                l["album"] = tag["album"][0]
                l["path"] = filename
                lista.append(l)
            except Exception as e:
                logging.error("Error con este archivo {} {}".format(filename, e))
        else:
            logging.info("Archivo no es audio {}".format(filename))
    
    def cpyArchivo(self, filnameIn):
        try:
            shutil.copy(filnameIn, self.dirOutput)
        except Exception as e:
            logging.error("Error al copiar archivo {} {}".format(filnameIn, e))

    def getLocalTracks(self):
        return self.localTracks