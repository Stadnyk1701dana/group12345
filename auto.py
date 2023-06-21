import datetime


class Auto:
    def __init__(self, year: int, manufacturer: str, brand: str, fuel: float) -> None:
       self.__year = year
       self.__manufacturer = manufacturer
       self.__brand = brand
       self.fuel = fuel
       self.race = 0

    def __str__(self):
        return f'AUTO: {self.__year}, {self.__manufacturer}, {self.__brand}, {self.race}, {self.fuel}'

    @property
    def age(self):
        auto_age = datetime.datetime.today().year - self.__year
        return auto_age

auto1 = Auto(1993, 'Toyota', 'Yaris', 7)
auto2 = Auto(2019, 'BMW', 'I7', 8)
auto3 = Auto(2015, 'Mercedes', 'B-class', 9)
print(auto1)
print('Auto1.age = ', auto1.age)
print(auto2)
print('Auto2.age = ', auto2.age)
print(auto3)
print('Auto3.age = ', auto3.age)

