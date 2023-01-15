



class Item(StatManagerClass):


    def __init__(self):

        super().__init__()


        self._exists = True

        
        self.callback = None


    def use(self, usager):

        if self.callback is not None:
            self.callback(self, usager)
            return True
        return False


    @staticmethod
    def FromFileById(path, id_):

        file_handler = open(path, "r", encoding="UTF-8")
        all_items = json.loads(file_handler.read())
        file_handler.close()

        item_attrs = all_items[id_]

        instance = ItemClass()
        instance.id = id_        
        for attr, value in item_attrs.items():

            setattr(instance, attr, value)

        return instance._copy()


    def copy(self):

        return deepcopy(self)
