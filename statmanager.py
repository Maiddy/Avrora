



class StatManager():


        def __init__(self):
        
            self.__tags = []


        def addStat(self, name=None, value=None):

            setattr(self, name, value)


        #def getStats(self):

            #return getattr()


        def hasStat(self, name):

            return True if name in dir(self) else False


        #def delStat(self, name):

            #if name in self._stats:
             #   return self._stats.pop(name)
            #return False


        def addTag(self, tag):

            if (tag not in self.__tags):
                self.__tags.append(name)
                return True
            return False


        def getTags(self):

            return self.__tags


        def hasTag(self, tag):

            return True if tag in self.__tags else False


        def delTag(self, tag):

            self.__tags.remove(tag)