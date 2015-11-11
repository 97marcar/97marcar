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
    def __init__(self, length):
        """..."""
        super().__init__("Interstellar", "SCI-FI", "Christoper Nolan", "2014")
        self.movie_type = "DVD"
        self.length = length
        
    
def main():
    item = DVD("123")
    print(item.info())
    
if __name__ == "__main__":
    main()