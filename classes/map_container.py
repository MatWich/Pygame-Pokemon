import os

from classes.map import Map
from config import *

class MapContainer:
    def __init__(self):
        self._allFgMapPaths = {}
        self._allBgMapPaths = {}

    def loadMapPaths(self) :
        map_names = [f for f in os.listdir(MAP_FOLDER) if os.path.isfile(os.path.join(MAP_FOLDER, f))]
        for map in map_names:
            key = map.split(".")[0]
            self._allFgMapPaths[key] = os.path.join(MAP_FOLDER, map)
        return self

    def getMap(self, name):
        return Map(self._allFgMapPaths[name])
