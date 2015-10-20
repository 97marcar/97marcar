# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:37:57 2015

@author: 97marcar
"""
from random import *

class Animals():
    """An animalclass"""
    
    def __init__(self, growth_rate, food_need, water_need, name):
        self.name = name
        self.weight = 50
        self.days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        self.water_need = water_need
        self.status = "baby"
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
        
        self.update_status()
    
    def auto_grow(self, animal, days):
        for day in range(days):
            if self.type == "Cow":
                self.food = randint(10,20)
                self.water = randint(10,20)
            elif self.type == "Sheep":
                self.food = randint(1,15)
                self.water = randint(1,15)
            self.grow(self.food, self.water)
        self.days_growing += days
                
def manual_grow(animal):
      valid = False
      
      while not valid:
        try:
          food = int(input("Please enter a food value (5-20): "))
          if 5 <= food <= 20:
            valid = True
          else:
            print("not a valid number please choose a number between 5 and 20")
        except ValueError:
           print("not a valid number please choose a number between 5 and 20")
           
      valid = False
      while not valid:
        try:
          water = int(input("Please enter a water value (5-20): "))
          if 5 <= water <= 20:
            valid = True
          else:
            print("not a valid number please choose a number between 5 and 20")
        except ValueError:
           print("not a valid number please choose a number between 5 and 20")
      animal.grow(food, water)
      animal.days_growing += 1
         
def display_menu():
    print("Here you can experiment on the animals.")
    print()
    print("1. Feed automaticlly for 30 days")
    print("2. Feed manually for 1 day")
    print("3. Report")
    print("0. Exit the farm")
    
def manage_animal(animal):
    noexit = False
    display_menu()
    while not noexit:
        
        choice = int(input("Your choice: "))
        if choice == 1:
            animal.auto_grow(animal, 30)
            
        elif choice == 2:
            manual_grow(animal)
            
        elif choice == 3:
            print(animal.report())
            
        elif choice == 0:
            noexit = True
            print("Thank you for using the experiment.")
            
        else:
            print("Select a valid option.")
        
def main():
    pass

    
if __name__ == "__main__":
    main()
            
            
            
            
            