class Person:  # Клас Особа
    def __init__(self):
        self.name = None  # прізвище
        self.byear = None  # рік народження

    def input(self):  # ввести особу
        self.name = input('Прізвище: ')
        self.byear = input('Рік народження: ')

    def print(self):  # вивести особу
        print(self.name, self.byear, end=' ')


routes = {
    ('Київ', 'Львів', 540.7),
    ('Київ', 'Харків', 489),
}
price = 1.5


class Passenger(Person):
    def __init__(self):
        self.name = None
        self.byear = None
        self.from_city = None
        self.to_city = None

    def input(self):
        self.name = input('Прізвище: ')
        self.byear = input('Рік народження: ')
        self.from_city = input('Місто відправлення: ')
        self.to_city = input('Місто прибуття: ')

    def print(self):
        print(self.name, self.byear, self.from_city, self.to_city, end=' ')

    def calculate(self):
        for route in routes:
            if (self.from_city == route[0] and self.to_city == route[1]) or (self.from_city == route[1] and self.to_city == route[0]):
                return route[2] * price


passengers = []
while True:
    passenger = Passenger()
    passenger.input()
    passengers.append(passenger)
    if input('Продовжити? (т/н) ') == 'н':
        break

for passenger in passengers:
    passenger.print()
    print(passenger.calculate())
