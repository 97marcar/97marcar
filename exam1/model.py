
from item import *
class Model:

    def __init__(self):
        """The constructor of the model"""
        self.lista_BR = [] #the list that will contain the Blueray movies
        self.lista_DVD = [] #the list that will contain the regular DVD movies
        self.lista_VHS = [] #the list that will contain the VHS movies
        
    def add_movie(self, movie):
        self.lista_DVD.append(movie)
            
            
            
def main():
    
    new_model = Model()
    item = DVD("3h", "Interstellar", "SCI-FI", "Christoper Nolan", "2014")
    new_model.add_movie(item)
    print(item.info())
    print(new_model.lista_DVD.info())
    
if __name__ == "__main__":
    main()