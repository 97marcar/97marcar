# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:28:22 2015

@author: marcu
"""

from animal_class import *

class Sheep(Animals):
    
    def __init__(self):
        super().__init__(2,5,5)
        self.type = "Sheep"
        self.weight = 20
        
    def grow(self, food, water):
        if food >= self.food_need and water >= self.water_need:
            if self.status == "Youngling" and food > self.food_need:
                self.weight += self.growth_rate*2
            elif self.status == "Young" and food >= self.food_need:
                self.weight += self.growth_rate*1.5
            else:
                self.weight += self.growth_rate
        self.update_status()
        
def main():
    sheep = Sheep()
    print(sheep.report())

if __name__ == "__main__":
    main()