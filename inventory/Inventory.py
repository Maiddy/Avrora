from random import randint
from copy import deepcopy
from classes.StatManagerClass import StatManagerClass
import json




class Inventory():


    def __init__(self, capacity=-1, matrix=(0, 0), auto_clear=True):

        self.capacity = capacity
        self.capacity_busy = 0
        
        self.matrix_size = matrix[0]*matrix[1]
        self.matrix_size_busy = 0
        
        self.items = []


    def put(self, item: ItemClass):
        #if is it free space here
        if self.capacity == -1:
        
            self.items.append(item)
            
        elif (self.matrix_size-self.matrix_size_busy) >= item.matrix_size:
        
            self.items.append(item)
            self.matrix_size_busy += item.matrix_size
        
        elif (self.capacity - self.capacity_busy) >= item.size:
        
            self.items.append(item)
            self.capacity_busy += item.size
            
        else:
            return False
        #if item added successfully
        return True


    def take(self, item: ItemClass):

        self.capacity_busy -= item.size
        return self.items.pop(self.items.index(item))


    def getItems(self):

        self.__update()
        return self.items


    def __update(self):

        to_remove = []
                
        for item in self.items:
            if item._exists == False:
                self.capacity_busy -= item.size
                to_remove.append(item)
        for item_to_remove in to_remove:
            self.items.remove(item_to_remove)



