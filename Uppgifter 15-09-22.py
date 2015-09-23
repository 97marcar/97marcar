# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:07:30 2015

@author: 97marcar
"""

class Crop:
  """A generic food crop"""
  
  #constructor
  def __init__(self, growth_rate, light_need, water_need):
    """konstruktor"""
    self._growth = 0
    self._days_growing = 0
    self._growth_rate = growth_rate
    self._light_need = light_need
    self._water_need = water_need
    self._status = "seed"
    self._type = "Generic"
    
  def needs(self):
    """status about how much light and water is needed."""
    return({'light need': self._light_need, 'water need': self._water_need})
    
  def report(self):
    return({'type': self._type, 'status': self._status, 'growth': self._growth, 'days growing': self._days_growing})

  def get_growth(self):
    """gives the user the value of growth"""
    return(self._growth)
  
  def set_growth(self,growth):
    """sets the value of """
    self._growth = growth
    
  def get_days_growing(self):
    """gives the user the value of days growing"""
    return(self.get_days_growing)
  
  def set_days_growing(self, days_growing):
    """sets the value of days growing"""
    self._days_growing = days_growing
    

  def get_growth_rate(self):
    """gives the user the value of the growth rate"""
    return(self._growth_rate)
  
  def set_growth_rate(self,growth_rate):
    """sets the value of the growth rate"""
    self._growth_rate = growth_rate
    
  def get_light_need(self):
    """gives the user the value of light needed"""
    return(self._light_need)
  
  def set_light_need(self,light_need):
    """sets the value of light needed"""
    self._light_need = light_need
    
  def get_water_need(self):
    """gives the user the value of water needed"""
    return(self._water_need)
  
  def set_water_need(self,water_need):
    """sets the value of water needed"""
    self._water_need = water_need
    
  def get_status(self):
    """gives the user the status of the crop"""
    return(self._status)
  
  def set_status(self,status):
    """sets the status of the crop"""
    self._status = status

  def get_type(self):
    """gives the user the type of the seed"""
    return(self._type)
  
  def set_type(self,new_type):
    """sets the type of the seed """
    self._type = new_type





def main():
   #instaniate the class
   new_crop = Crop(1,4,3)
   print(new_crop.get_status())
   print(new_crop.get_growth())
   print(new_crop.get_light_need())
   print(new_crop.get_water_need())
   print(new_crop.report())
   print(new_crop.needs())
   new_crop2 = Crop(2,5,7)
   print(new_crop2.get_status())
   print(new_crop2.get_light_need())
   print(new_crop2.get_water_need())
   
   help(Crop)
   
if __name__ == "__main__":
  main()