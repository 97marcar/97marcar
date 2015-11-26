
class Item:
    """Creates a base of an item class"""
    def __init__(self, name, genre, director, year):
        """The constructor of the Item class"""
        self.movie_type = "movie"
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year

        
class DVD(Item):
    """Uses the Item class to make a DVD to add to the register"""
    def __init__(self, length, name, genre, director, year):
        """The constructor of the DVD class"""
        super().__init__(name, genre, director, year)
        self.movie_type = "DVD"
        self.length = length
        
    def __str__(self):
        return(self.name+";"+self.genre+";"+self.director+";"+self.year+";"+self.length+";"+"\n")
        
class BR(Item):
    """Uses the Item class to make a Blueray to add to the register"""
    def __init__(self, resolution, name, genre, director, year):
        """The constructor of the BR class"""
        super().__init__(name, genre, director, year)
        self.movie_type = "Blueray"
        self.resolution = resolution
        
    def __str__(self):
        return(self.name+";"+self.genre+";"+self.director+";"+self.year+";"+self.resolution+";"+"\n")

class VHS(Item):
    """Uses the Item class to make a VHS to add to the register"""
    def __init__(self, color, name, genre, director, year):
        """The constructor for the VHS class"""
        super().__init__(name, genre, director, year)
        self.movie_type = "VHS"
        self.color = color
           
    def __str__(self):
        return(self.name+";"+self.genre+";"+self.director+";"+self.year+";"+self.color+";"+"\n")
    