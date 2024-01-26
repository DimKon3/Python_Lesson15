class Transport:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def get_data(self):
        print (f"Название автомобиля: {self.name}, Скорость: {self.max_speed}, Пробег: {self.mileage}")


class Avtobus(Transport):
    
    def seating_capacity(self, capacity = 50):
        return f"Вместимость одного автобуса {self.name} = {capacity}"


Avtobus1 = Avtobus("Renault Logan", 180, 5)
Avtobus1.get_data()
print(Avtobus1.seating_capacity())
Avtobus2 = Avtobus("Icarus", 140, 12)
Avtobus2.get_data()
print(Avtobus2.seating_capacity(70))