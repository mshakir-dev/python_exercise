# Map (f, data)
import math
def area(r):
  return math.pi * (r**2)
print(area(2))
print("******************************")
radius_list = [2,5,7.1,0.5,12]
areas = []
for r in radius_list:
    # Call Radius Function and Round Values by Using Math Floor Function
  a = math.floor(area(r))
  areas.append(a)
print(areas)