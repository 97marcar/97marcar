
from item import *
class Model:

    def __init__(self):
        """The constructor of the model"""
        self.lista_BR = [] #the list that will contain the Blueray movies
        self.lista_DVD = [] #the list that will contain the regular DVD movies
        self.lista_VHS = [] #the list that will contain the VHS movies
        
    def add_movie(self, movie):
        self.lista_DVD.append(movie)
            
            
            
    def create_item(self, movie_type, unique, name, genre, director, year):
        if movie_type == "DVD":
            self.dvd = DVD(unique, name, genre, director, year)
            print(self.dvd.info())
        if movie_type == "Blueray":
            self.br = BR(unique, name, genre, director, year)
            print(self.br.info())
        if movie_type == "VHS":
            self.vhs = VHS(unique, name, genre, director, year)
            print(self.vhs.info())
        
        self.item = DVD("3h", "Interstellar", "SCI-FI", "Christoper Nolan", "2014")
        self.add_movie(self.item)
