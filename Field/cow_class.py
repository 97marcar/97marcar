# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:14:40 2015

@author: marcu
"""

from animal_class import *

class Cow(Animals):
    
    def __init__(self, name):
        super().__init__(5,10,10, name)
        self.type = "Cow"
        
        
    def grow(self, food, water):
        if food >= self.food_need and water >= self.water_need:
            if self.status == "Youngling" and food+5 >= self.food_need:
                self.weight += self.growth_rate*2
            elif self.status == "Young" and food+5 >= self.food_need:
                self.weight += self.growth_rate*1.5
            else:
                self.weight += self.growth_rate
        self.update_status()
        
def main():
    cow = Cow()
    print(cow.report())

if __name__ == "__main__":
    main()