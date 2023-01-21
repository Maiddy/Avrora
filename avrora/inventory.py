from avrora.statmanager import StatManager
from copy import deepcopy




class Inventory(StatManager):


    def __init__(self):

        super().__init__()
            
        self._items = []
        self.wrapper = None


    def setWrapper(self, func):

        self.wrapper = func


    def getItems(self):

        return self._items


    def add(self, item):

        self._items.append(item.copy())


    #def remove()


    def push(self, item):

        if self.wrapper is not None: return self.wrapper(self, "push", item)
        self.add(item)


    def take(self, item):

        self._update()
        if self.wrapper is not None: return self.wrapper(self, "take", item)
        return self._items.pop(item)


    def _update(self):

        to_remove = []
        for item in self._items:
            if not item._exists:
                to_remove.append(item)

        for item_to_rem in to_remove:
            self._items.remove(item_to_rem)




class Item(StatManager):


    def __init__(self):

        super().__init__()

        self._exists = True
        self.callback = None


    def use(self, usager=None):

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

        item = Item()
        item.id = id_

        for attr, value in item_attrs.items():

            setattr(item, attr, value)

        return instance.copy()


    def copy(self):

        return deepcopy(self)





















































