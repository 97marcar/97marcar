# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:37:57 2015

@author: 97marcar
"""
from random import *

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
        self.food = 0
        self.water = 0
        
    def needs(self):
        """return the food and water needed for the animal"""
        return({"food need": self.food_need, "water need": self.water_need})
        
    def report(self):
        return({'type': self.type, 'status': self.status, 'weight': self.weight, 'days growing': self.days_growing})
        print(str(self.growth_rate()))
        
    def update_status(self):
        if self.weight > 100:
            self.status = "Old"
        elif self.weight > 70:
            self.status = "Mature"
        elif self.weight > 60:
            self.status = "Young"
        elif self.weight > 50:
            self.status = "Youngling"
        elif self.weight == 50:
            self.status = "Baby"
        
            
    def grow(self, food, water):
        if food >= self.food_need and water >= self.water_need:
            self.weight += self.growth_rate
        self.days_growing += 1
        
        self.update_status()
    
    def auto_grow(self ,animal, days):
        for n in range(days):
            if self.type == ("Cow"):
                self.food == randint(5,15)
                self.water == randint(5,15)
                animal.grow(self.food, self.water)
            elif self.type == ("Sheep"):
                self.food == randint(1,10)
                self.water == randint(1,10)
                animal.grow(self.food, self.water)
        
    

        
def display_menu():
    print("Here you can experiment on the animals.")
    print()
    print("1. Feed automaticlly for 30days")
    print("2. Feed manually for 1 day")
    print("0. Exit the farm")
    
def manage_animal(animal):
    display_menu()
    choice = int(input("Your choice: "))
    if choice == 1:
        animal.auto_grow(animal, 30)
        print(animal.report())
    else:
        print("Thank you for using the experiment.")
        
    
        
def main():
    pass
    
if __name__ == "__main__":
    main()
            
            
            
            
            