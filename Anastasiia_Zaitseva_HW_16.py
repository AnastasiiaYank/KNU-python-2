# Описуємо клас Професія
class Profession:
    def __init__(self, name, specialty):
        self.name = name  # назва професії
        self.specialty = specialty  # спеціальність за освітою

    def create_profession(self):
        self.name = input("Введіть назву професії: ")
        self.specialty = input("Введіть спеціальність за освітою: ")

    def display_profession(self):
        print("Назва професії:", self.name)
        print("Спеціальність за освітою:", self.specialty)

# Описуємо клас РангДержслужби


class RankCivilService:
    def __init__(self, number, requirements):
        self.number = number  # номер рангу
        self.requirements = requirements  # вимоги для отримання рангу

    def create_rank(self):
        self.number = input("Введіть номер рангу: ")
        self.requirements = input("Введіть вимоги для отримання рангу: ")

    def display_rank(self):
        print("Номер рангу:", self.number)
        print("Вимоги для отримання рангу:", self.requirements)

# Описуємо клас ДержавнаПосада


class StatePosition(Profession, RankCivilService):
    def __init__(self, name, salary):
        self.name = name  # назва державної посади
        self.salary = salary  # заробітна плата

    def create_state_position(self):
        self.create_profession()
        self.create_rank()
        self.name = input("Введіть назву державної посади: ")
        self.salary = input("Введіть заробітну платню: ")

    def display_state_position(self):
        self.display_profession()
        self.display_rank()
        print("Назва державної посади:", self.name)
        print("Заробітна плата:", self.salary)


# Описуємо програму проведення конкурсу на перелік державних посад
positions = []  # список державних посад

while True:
    choice = input(
        "Введіть 'додати' для додавання державної посади, або 'вийти' для завершення програми: ")
    if choice == "додати":
        position = StatePosition("", "")
        position.create_state_position()
        positions.append(position)
    elif choice == "вийти":
        break

# Виводимо список державних посад
for position in positions:
    position.display_state_position()
