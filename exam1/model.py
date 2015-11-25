
from item import *
class Model:

    def __init__(self):
        """The constructor of the model"""
        self.lista_BR = [] #the list that will contain the Blueray movies
        self.lista_DVD = [] #the list that will contain the regular DVD movies
        self.lista_VHS = [] #the list that will contain the VHS movies

        
            
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
            
    def get_itemsBR(self):
        return self.lista_BR
        
        
    def get_itemsDVD(self):
        return self.lista_DVD
        
    def get_itemsVHS(self):
        return self.lista_VHS
        
    def set_saveBR(self):
        try:
            file = open("./saveBR.csv", "w")
        except:
            print("Wrong when saving to file.")
        else:
            for item in self.lista_BR:
                file.write(item.__str__())
            
            file.close() 
            
    def get_saveBR(self):
        try:        
            file = open("./saveBR.csv", "r")
        except:
            print("Wrong when opening file.")
        else:
            for line in file:
                line.strip()
                item = line.split(";")
                self.lista_BR.append(BR(item[4], item[1], item[2], item[3], item[0]))
            file.close()
            
    def set_saveDVD(self):
        try:
            file = open("./saveDVD.csv", "w")
        except:
            print("Wrong when saving to file.")
        else:
            for item in self.lista_DVD:
                file.write(item.__str__())
            
            file.close() 
            
    def get_saveDVD(self):
        try:        
            file = open("./saveDVD.csv", "r")
        except:
            print("Wrong when opening file.")
        else:
            for line in file:
                line.strip()
                item = line.split(";")
                self.lista_DVD.append(DVD(item[4], item[1], item[2], item[3], item[0]))
            file.close()
            
    def set_saveVHS(self):
        try:
            file = open("./saveVHS.csv", "w")
        except:
            print("Wrong when saving to file.")
        else:
            for item in self.lista_VHS:
                file.write(item.__str__())
            
            file.close() 
            
    def get_saveVHS(self):
        try:        
            file = open("./saveVHS.csv", "r")
        except:
            print("Wrong when opening file.")
        else:
            for line in file:
                line.strip()
                item = line.split(";")
                self.lista_VHS.append(VHS(item[4], item[1], item[2], item[3], item[0]))
            file.close()