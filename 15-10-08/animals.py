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
    print("0. Exit the farm")
    
def menu_choice():
    display_menu()
    choice = int(input("Your choice please: "))
    noexit = True
    while noexit:
        if choice == 1:
            animal = Cow()
            noexit = False
        elif choice == 2:
            animal = Sheep()
            noexit = False
        elif choice == 0:
            print("Good bye.")
            noexit = False
        else:
            print("Please select a vaild option.")
        
    return animal
    
def main():
    
    animal = menu_choice()
    manage_animal(animal)
    
if __name__ == "__main__":
    main()
    