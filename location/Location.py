from Avrora.statmanager import StatManager
from copy import deepcopy




class Location(StatManager, ):


        def __init__(self):

            super().__init__()


        def FromFileById(self, path, id_):
    
            file_handler = open(path, "r", encoding="UTF-8")
            all_locations = json.loads(file_handler.read())
            file_handler.close()
            
            location = all_locations[id_]
            instance = self.Location()
            instance.id = id_
            for attr, value in location.items():
            
                setattr(instance, attr, value)
    
            return deepcopy(instance)
