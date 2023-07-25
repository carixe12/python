import math

def check_coin_in_circle(x, y, r):
    
    distance_from_center = math.sqrt(x**2 + y**2)
    return distance_from_center <= r



print("Enter coin coordinates:")
x = float(input("x: "))
y = float(input("y: "))
r = float(input("Enter radius: "))

if check_coin_in_circle(x, y, r):
    print("The coin is somewhere nearby.")
else:
    print("There are no coins in the area.")