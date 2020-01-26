from path import *

class User:
    def __init__(self, current=Location(), path=None, id=0):
        self.id = id
        self.current = current
        self.path = path
    
    def get_path(self):
        return self.path
    
    def set_path(self, path):
        self.path = path

    def get_current(self):
        return self.current

    def set_current(self, current):
        self.current = current

    
    