# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:07:52 2015

@author: 97marcar
"""

from crop_class import *

class Potato(Crop):
  """A potato crop"""
  
  
  #constructor
  def __init__(self):
    #call parent class constructor with default values for potato
    #growth rate = 1, light neeed 3, water need 6
      super().__init__(1,3,6)
      self._type = "Potato"
    
  #override grow method for subclass
  def grow(self,light,water):
      if light >= self._light_need and water >= self._water_need:
        if self._status == "Seedling" and water > self._water_need:
          self._growth += self._growth_rate * 1.5
        elif self._status == "Young" and water > self._water_need:
          self._growth += self._growth_rate * 1.25
        else:
          self._growth += self._growth_rate
      #increament day growing
      self._days_growing += 1
      self._update_status()
          
  
def main():
  #Crate a new potato crop
  potato_crop = Potato()
  print(potato_crop.report())
  #manually grow the crop
  manual_grow(potato_crop)
  print(potato_crop.report())
  manual_grow(potato_crop)
  print(potato_crop.report())
  
if __name__ == "__main__":
  main()