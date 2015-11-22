
from item import *
class Model:

    def __init__(self):
        """The constructor of the model"""
        self.lista_BR = [] #the list that will contain the Blueray movies
        self.lista_DVD = [] #the list that will contain the regular DVD movies
        self.lista_VHS = [] #the list that will contain the VHS movies
        self.create_item()
        
    def add_movie(self, movie):
        self.lista_DVD.append(movie)
            
            
            
    def create_item(self):
        self.item = DVD("3h", "Interstellar", "SCI-FI", "Christoper Nolan", "2014")
        self.add_movie(self.item)
