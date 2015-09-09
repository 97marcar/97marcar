# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:31:25 2015

@author: 97marcar
"""
#Uppgift 1
for n in range(1, 16):
  print(n)
  
#Uppgift 2
for n in range(20, 31):
  print(n)
  
#Uppgift 3
for n in range(0, 1001):
  print(n, '', end='')

print()
#Uppgift 4
for n in range(10, -11, -1):
  print(n)
  
#Uppgift 5
print("tal", "\t", "tal^2", "\t", "tal^3")
for n in range(21):
  print("   --------------------------")
  print(str(n).rjust(5), '\t', str(n**2).rjust(5), '\t', str(n**3).rjust(5), end='')
  print()
print("   --------------------------")
  
#Uppgift 6
for n in range(5):
  for n in range (10):
    print(n, '',end="")
  print('\n')    
  