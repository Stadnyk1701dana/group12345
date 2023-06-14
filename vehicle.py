from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, model: str, tank_volume: int, fuel: float, speed: float, race:int, trans_fuel:float):
        self.model = model
        self.tank_volume = tank_volume
        self.fuel = fuel
        self.speed = speed
        self.race = race
        self.trans_fuel = trans_fuel

    def charge(self):
        add_fuel = 20
        if self.fuel + add_fuel <= self.tank_volume:
            self.fuel += add_fuel
        else:
            self.fuel += self.tank_volume-self.fuel
        return self.fuel

    def transfusion(self, other):
        if other.tank_volume - other.fuel >= self.trans_fuel and self.fuel >= self.trans_fuel:
            other.fuel += self.trans_fuel
        if other.tank_volume - other.fuel >= self.trans_fuel and self.fuel <= self.trans_fuel:
            other.fuel += self.fuel
        if other.tank_volume - other.fuel < self.trans_fuel and self.trans_fuel <= self.fuel:
            other.fuel += other.tank_volume - other.fuel
        return other.fuel


    @abstractmethod
    def __str__(self):
        pass

class auto(Vehicle):

    def __init__(self, model: str, tank_volume: int, fuel: float, speed: float, race:int, pas_number: int, airbag: bool, trans_fuel: float):
        super().__init__(model, tank_volume, fuel, speed, race, trans_fuel)
        self.pas_number = pas_number
        self.airbag = airbag

    def __str__(self):
        return f'I am an auto {self.model}'

class moto(Vehicle):

    def __init__(self, model: str, tank_volume: int, fuel: float, speed: float, race: int, carriage: bool, trans_fuel: float):
        super().__init__(model, tank_volume, fuel, speed, race, trans_fuel)
        self.carriage = carriage

    def __str__(self):
        return f'I am a moto with fuel: {self.fuel}'

auto1 = auto(model='toyota', tank_volume = 50, fuel = 30, speed = 270, race = 240000, pas_number = 5, airbag = True, trans_fuel = 32.654)
moto1 = moto(model='suzuki', tank_volume = 30, fuel = 15, speed = 300, race = 100000, carriage = True, trans_fuel=20)
auto1.charge()
auto1.transfusion(moto1)

pass
