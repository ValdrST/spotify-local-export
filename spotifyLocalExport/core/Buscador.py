class Buscador():
    def __init__(self):
        self.listaPath = []

    def buscar(self, spotifyList, localList):
        for trackSp in spotifyList:
            res = next((sub for sub in localList if sub['titulo'] == trackSp['titulo']), None)
            if res != None:
                self.listaPath.append(res["path"])
                spotifyList.remove(trackSp)
        return spotifyList
    
    def getListaPath(self):
        return self.listaPath

if __name__ == "__main__":
    b = Buscador()
    spotifyList = [
        {"titulo": "Dr. Stein", "artista": "Helloween", "album": "Keeper of the Seven Keys, Pt. II (Expanded Edition)"}, 
        {"titulo": "Emerald Sword", "artista": "Rhapsody", "album": "Symphony of Enchanted Lands"}, 
        {"titulo": "Rasputin", "artista": "Turisas", "album": "Rasputin"}, 
        {"titulo": "As Samhain Comes", "artista": "Waylander", "album": "\u00c9ri\u00fa's Wheel"}, 
        {"titulo": "I, Caligvla", "artista": "Ex Deo", "album": "Caligvla"}, 
        {"titulo": "Spiritual Healing", "artista": "Death", "album": "Spiritual Healing (Deluxe Version)"}, 
        {"titulo": "Solskinnsmedisin", "artista": "Trollfest", "album": "Kaptein Kaos"}, 
        {"titulo": "Villanden", "artista": "Trollfest", "album": "Villanden"}, 
        {"titulo": "Trollhammaren", "artista": "Finntroll", "album": "Nattf\u00f6dd"}
    ]
    localList = [
        {"titulo": "Dr. Stein", "artista": "Helloween", "album": "Keeper of the Seven Keys, Pt. II (Expanded Edition)", "path":"1"}, 
        {"titulo": "Dr. Stein", "artista": "Helloween", "album": "Keeper of the Seven Keys, Pt. II (Expanded Edition)", "path":"2"},
        {"titulo": "Emeral Sword", "artista": "Rhapsody", "album": "Symphony of Enchanted Lands", "path":"1"}, 
        {"titulo": "Rasputin", "artista": "Turisas", "album": "Rasputin", "path":"2"}, 
        {"titulo": "As Smhain Comes", "artista": "Waylander", "album": "\u00c9ri\u00fa's Wheel", "path":"1"}, 
        {"titulo": "I, aligvla", "artista": "Ex Deo", "album": "Caligvla", "path":"1"}, 
        {"titulo": "Spritual Healing", "artista": "Death", "album": "Spiritual Healing (Deluxe Version)", "path":"1"}, 
        {"titulo": "Slskinnsmedisin", "artista": "Trollfest", "album": "Kaptein Kaos", "path":"1"}, 
        {"titulo": "illanden", "artista": "Trollfest", "album": "Villanden", "path":"1"}, 
        {"titulo": "Tollhammaren", "artista": "Finntroll", "album": "Nattf\u00f6dd", "path":"1"}
    ]
    print(b.buscar(spotifyList, localList))
