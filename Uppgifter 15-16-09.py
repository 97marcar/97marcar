# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:07:30 2015

@author: 97marcar
"""

class Crop:
  """A generic food crop"""
  
  #constructor
  def __init__(self, growth_rate, light_need, water_need):
    self._growth = 0
    self._days_growing = 0
    self._growth_rate = growth_rate
    self._light_need = light_need
    self._water_need = water_need
    self._status = "seed"
    self._type = "Generic"
    
def main():
   #instaniate the class
   new_crop = Crop(1,4,3)
   print(new_crop._status)
   print(new_crop._light_need)
   print(new_crop._water_need)
   new_crop2 = Crop(2,5,7)
   print(new_crop2._status)
   print(new_crop2._light_need)
   print(new_crop2._water_need)
   
if __name__ == "__main__":
  main()