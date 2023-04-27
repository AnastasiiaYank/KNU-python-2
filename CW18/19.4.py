from abc import ABC, abstractmethod
import random


class Creature(ABC):
    def __init__(self, age, lifespan, growth_method, feeding_method, required_food, reproduction_rate, reproduction_conditions):
        self.age = age
        self.lifespan = lifespan
        self.growth_method = growth_method
        self.feeding_method = feeding_method
        self.required_food = required_food
        self.reproduction_rate = reproduction_rate
        self.reproduction_conditions = reproduction_conditions

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def reproduce(self):
        pass


class Animal(Creature):
    def __init__(self, age, lifespan, growth_method, feeding_method, required_food, reproduction_rate, reproduction_conditions, movement_speed):
        super().__init__(age, lifespan, growth_method, feeding_method,
                         required_food, reproduction_rate, reproduction_conditions)
        self.movement_speed = movement_speed

    def grow(self):
        self.age += self.growth_method

    def reproduce(self):
        if random.random() < self.reproduction_rate:
            return Animal(0, self.lifespan, self.growth_method, self.feeding_method, self.required_food, self.reproduction_rate, self.reproduction_conditions, self.movement_speed)
        else:
            return None


class Herb(Creature):
    def __init__(self, age, lifespan, growth_method, feeding_method, required_food, reproduction_rate, reproduction_conditions, height):
        super().__init__(age, lifespan, growth_method, feeding_method,
                         required_food, reproduction_rate, reproduction_conditions)
        self.height = height

    def grow(self):
        self.age += self.growth_method
        self.height += self.growth_method

    def reproduce(self):
        if random.random() < self.reproduction_rate:
            return Herb(0, self.lifespan, self.growth_method, self.feeding_method, self.required_food, self.reproduction_rate, self.reproduction_conditions, self.height)
        else:
            return None


class Simulation:
    def __init__(self, animal_classes, herb_classes, initial_config):
        self.animal_classes = animal_classes
        self.herb_classes = herb_classes
        self.config = initial_config

    def run(self, T):
        for t in range(T):
            new_config = {}
            for animal_class in self.animal_classes:
                new_config[animal_class] = []
                for animal in self.config[animal_class]:
                    animal.grow()
                    food_available = 0
                    for herb_class in self.herb_classes:
                        for herb in self.config[herb_class]:
                            if herb.feeding_method == animal.feeding_method:
                                food_available += herb.required_food
                    if food_available >= animal.required_food:
                        new_config[animal_class].append(animal)
                        animal_to_reproduce = animal.reproduce()
                        if animal_to_reproduce is not None:
                            new_config[animal_class].append(
                                animal_to_reproduce)
            for herb_class in self.herb_classes:
                new_config[herb_class] = []
                for herb in self.config[herb_class]:
                    herb.grow()
                    new_config[herb_class].append(herb)
                    herb_to_reproduce = herb.reproduce()
                    if herb_to_reproduce is not None:
                        new_config[herb_class].append(herb_to_reproduce)
            self.config = new_config


initial_config = {
    Animal: [Animal(0, 10, 1, "meat", 2, 0.5, "nearby", 5), Animal(0, 10, 1, "plants", 1, 0.5, "nearby", 3)],
    Herb: [Herb(0, 5, 0.5, "sunlight", 1, 0.3, "nearby", 1),
           Herb(0, 5, 0.5, "sunlight", 1, 0.3, "nearby", 1)]
}

simulation = Simulation([Animal], [Herb], initial_config)
simulation.run(10)
