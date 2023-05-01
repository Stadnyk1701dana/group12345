r=int(input("Введіть радіус "))

print("Коди умов до задачі: 1 -довжина кола, 2 - площа круга, 3 - обєм кулі" )

cod=int(input("Введіть код до задачі, яку слід виконати "))

print("При r=",r)

if cod==1:

      l=2*math.pi*r

      print("Довжина кола - ",round(l,2))

elif cod==2:

      s=math.pi*r*r

      print("Площа круга - ",round(s,2))

elif cod==3:

      v=4/3*math.pi*math.pow(r,3)

      print("Обєм кулі - ",round(v,2))