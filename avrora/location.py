from Avrora.statmanager import StatManager
from copy import deepcopy




class Location(StatManager):


    def __init__(self):

        super().__init__()


    @staticmethod
    def FromFileById(id_):

        return




class LocationManager(StatManager):


    def __init__(self):

        super().__init__()

        self.game_map = {}
        self.locs_with_chars = {}


    #def loadMapFromFile(self, path):

        #file_handler = open(path. "r", encoding="UTF-8")


        #file_handler.close()


    def changeLocationTo(self, new_location, character):

        pass


    def add(self, location):

        pass


    def changeLocationManager(self, character, newManager):

        pass


    def getParentWithChild(self, d):
    
        result = []
        for key, value in d.items():
            if value is not None:
                ava = list(value.keys())
            else:
                result.append((key, None))
                continue
            for i in ava:
                result.append((key, i))
                if isinstance(d[key][i], dict):
                    result.extend(getParentWithChild(d[key]))    

        return result
    
    
    def getAvailableLocations(self, cur_location, locas):
    
        result = []
        for couple in getParentWithChild(locas):
            if couple[0] == cur_location:
                result.append(couple[1])
            elif couple[1] == cur_location:
                result.append(couple[0])
        
        return result
