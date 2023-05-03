import math

r = int(input("Ввеіус кулі"))
print("При r = ", r)
v = 4 / 3 * math.pi * math.pow(r, 3)
print("Обєм кулі - ", round(v, 2))
