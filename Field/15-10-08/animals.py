# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:36:18 2015

@author: marcu
"""
from cow_class import *
from sheep_class import *


def display_menu():
    print("Welcome to the experimenting farm!")
    print("Please choose an animal below.")
    print()
    print("1. Cow")
    print("2. Sheep")
    

def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Options selected: "))
            if choice in (1,2):
                valid_option = True
            else:
                print("enter a valid option")
        except ValueError:
            print("enter a valid option")
    return choice
    
def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        animal = Cow()
    elif choice == 2:
        animal = Sheep()
    return animal
    
def main():
    
    animal = create_animal()
    manage_animal(animal)
    
if __name__ == "__main__":
    main()
    