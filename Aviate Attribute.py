"""
Please note that all attributes should be converted from confidible source, for example, Jane's publications.

"""

class Aviate():
 def __init__(self, name, speed, missles, fighting_range, radar, EMV):
  self.name = name
  self.speed= speed
  self.missles=missles
  self.fighting_range=fighting_range
  self.radar=radar
  self.EMV=EMV
  
#建立一個名叫F-16-V的Aviate實體(物件),單位分別是km/hr,unit,km,km,km
f_F16V= Aviate('F-16-V',10,8,20,10,5) 
