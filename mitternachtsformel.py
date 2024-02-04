import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c

if D < 0:
    print("Unlösbar!")
elif D==0:
    x = (-b + math.sqrt(D))/(2*a)
    print(f"x = {x}")
else:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b + math.sqrt(D))/(2*a)
print(f"x1 = {x1}\nx2 = {x2}")