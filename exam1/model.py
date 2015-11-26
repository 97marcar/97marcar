import test
from item import *
class Model:

    def __init__(self):
        """The constructor of the model"""
        self.lista_BR = [] #the list that will contain the Blueray movies
        self.lista_DVD = [] #the list that will contain the regular DVD movies
        self.lista_VHS = [] #the list that will contain the VHS movies

        
            
    def create_item(self, movie_type, unique, name, genre, director, year):
        """Creates an item from the item.py and adds them to a list"""
        self.colorfalsecheck = True
        self.yearfalsecheck = True
        try:
            if test.check_valid_year(int(year)) == True:
                if movie_type == "DVD":
                    self.dvd = DVD(unique, name, genre, director, year)
                    self.lista_DVD.append(self.dvd)
                if movie_type == "Blueray":
                    self.br = BR(unique, name, genre, director, year)
                    self.lista_BR.append(self.br)
                if movie_type == "VHS":
                    if test.check_color_yes_no(str(unique)) == True:
                        self.vhs = VHS(unique, name, genre, director, year)
                        self.lista_VHS.append(self.vhs)
                    else:
                        self.colorfalsecheck = False
            else:
                self.yearfalsecheck = False
        except ValueError:
            self.yearfalsecheck = False
            
    def edit_item(self, movie_type, unique, name, genre, director, year, index):
        """Edits a selected item"""
        self.colorfalsecheck = True
        self.yearfalsecheck = True
        try:
            if test.check_valid_year(int(year)) == True:
                if movie_type == "DVD":
                    self.lista_DVD[index] = DVD(unique, name, genre, director, year)
                if movie_type == "Blueray":
                    self.lista_BR[index] = BR(unique, name, genre, director, year)
                if movie_type == "VHS":
                    if test.check_color_yes_no(str(unique)) == True:
                        self.lista_VHS[index] = VHS(unique, name, genre, director, year)
                    else:
                        self.colorfalsecheck = False
            else:
                self.yearfalsecheck = False
        except ValueError:
            self.yearfalsecheck = False
            
    def get_itemsBR(self):
        """returns the Blueraylist"""
        return self.lista_BR
        
        
    def get_itemsDVD(self):
        """returns the DVDlist"""
        return self.lista_DVD
        
    def get_itemsVHS(self):
        """returns the VHSlist"""
        return self.lista_VHS
        
    def set_saveBR(self):
        """Saves the Bluraylist"""
        try:
            file = open("./saveBR.csv", "w")
        except:
            print("Wrong when saving to file.")
        else:
            for item in self.lista_BR:
                file.write(item.__str__())
            
            file.close() 
            
    def get_saveBR(self):
        """Gets the saved BR-movies and adds them back to list"""
        try:        
            file = open("./saveBR.csv", "r")
        except:
            print("Wrong when opening file.")
        else:
            for line in file:
                line.strip()
                item = line.split(";")
                self.lista_BR.append(BR(item[4], item[0], item[1], item[2], item[3]))
            file.close()
            
    def set_saveDVD(self):
        """Saves the DVDlist"""
        try:
            file = open("./saveDVD.csv", "w")
        except:
            print("Wrong when saving to file.")
        else:
            for item in self.lista_DVD:
                file.write(item.__str__())
            
            file.close() 
            
    def get_saveDVD(self):
        """Gets the saved DVD-movies and adds them back to list"""
        try:        
            file = open("./saveDVD.csv", "r")
        except:
            print("Wrong when opening file.")
        else:
            for line in file:
                line.strip()
                item = line.split(";")
                self.lista_DVD.append(DVD(item[4], item[0], item[1], item[2], item[3]))
            file.close()
            
    def set_saveVHS(self):
        """Saves the VHSlist"""
        try:
            file = open("./saveVHS.csv", "w")
        except:
            print("Wrong when saving to file.")
        else:
            for item in self.lista_VHS:
                file.write(item.__str__())
            
            file.close() 
            
    def get_saveVHS(self):
        """Gets the saved VHS-movies and adds them back to list"""
        try:        
            file = open("./saveVHS.csv", "r")
        except:
            print("Wrong when opening file.")
        else:
            for line in file:
                line.strip()
                item = line.split(";")
                self.lista_VHS.append(VHS(item[4], item[0], item[1], item[2], item[3]))
            file.close()