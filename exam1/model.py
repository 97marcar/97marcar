
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
            self.lista_DVD.append(self.dvd)
            print(self.dvd.info())
        if movie_type == "Blueray":
            self.br = BR(unique, name, genre, director, year)
            self.lista_BR.append(self.br)
            print(self.br.info())
        if movie_type == "VHS":
            self.vhs = VHS(unique, name, genre, director, year)
            self.lista_VHS.append(self.vhs)
            print(self.vhs.info())
            
    def get_item(self):
        return self.lista_BR
            
