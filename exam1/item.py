
class Item:
    
    def __init__(self, name, genre, director, year):
        """..."""
        self.movie_type = "movie"
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
    
    def info(self):
        """..."""
        return({"type": self.movie_type, "Name": self.name, "Genre": self.genre, "Director": self.director, "Year": self.year})
        
class DVD(Item):
    """..."""
    def __init__(self, length, name, genre, director, year):
        """..."""
        super().__init__(name, genre, director, year)
        self.movie_type = "DVD"
        self.length = length
        
    def info(self):
        """..."""
        return({"type": self.movie_type, "Name": self.name, \
        "Genre": self.genre, "Director": self.director, \
        "Year": self.year, "Length": self.length})
        
class BR(Item):
    """..."""
    def __init__(self, resolution, name, genre, director, year):
        """..."""
        super().__init__(name, genre, director, year)
        self.movie_type = "Blueray"
        self.resolution = resolution
        
    def info(self):
        """..."""
        return({"type": self.movie_type, "Name": self.name, \
        "Genre": self.genre, "Director": self.director, \
        "Year": self.year, "Resolution": self.resolution})

class VHS(Item):
    """..."""
    def __init__(self, color, name, genre, director, year):
        """..."""
        super().__init__(name, genre, director, year)
        self.movie_type = "DVD"
        self.color = color
        
    def info(self):
        """..."""
        return({"type": self.movie_type, "Name": self.name, \
        "Genre": self.genre, "Director": self.director, \
        "Year": self.year, "Color": self.color})
    
def main():
    item = DVD("3h", "Shrek the third", "Animation", "Chris Miller", "2007")
    item1 = BR("1080p", "Interstellar", "SCI-FI", "Christoper Nolan", "2014")
    item2 = VHS("Yes", "Lord of the Rings", "Fantasy", "Peter Jackson", "2001")
    print()
    print(item.info())
    print()
    print(item1.info())
    print()
    print(item2.info())
    
if __name__ == "__main__":
    main()