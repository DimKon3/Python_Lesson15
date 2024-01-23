class Transport:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def get_data(self):
        print(f"Название автомобиля: {self.name}, Скорость: {self.max_speed}, Пробег: {self.mileage}")

Avtobus = Transport("Renault Logan", 180, 5)
Avtobus.get_data()