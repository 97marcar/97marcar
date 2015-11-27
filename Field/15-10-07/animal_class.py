# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:37:57 2015

@author: 97marcar
"""

class Animals():
    """An animalclass"""
    
    def __init__(self, growth_rate, food_need, water_need):
        self.weight = 50
        self.days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        self.water_need = water_need
        self.status = "status"
        self.type = "animal"
        self.name = "name"
        
    def needs(self):
        """return the food and water needed for the animal"""
        return({"food need": self.food_need, "water need": self.water_need})
        
    def report(self):
        return({'type': self.type, 'status': self.status, 'weight': self.weight, 'days growing': self.days_growing})
        
    def update_status(self):
        if self._growth > 20:
            self.status = "Old"
        elif self.growth > 10:
            self.status = "Mature"
        elif self.growth > 5:
            self.status = "Young"
        elif self.growth > 0:
            self.status = "Youngling"
        elif self.status == 0:
            self.status = "Baby"
            
    def grow(self, food, water):
        if food >= self.food_need and water >= self.water_need:
            self.weight += self.growth_rate
        self.days_growing += 1
        self.update_status()
        
def main():
    animal = Animals(5, 10, 10)
    print(animal.report())
    
if __name__ == "__main__":
    main()
            
            
            
            
            