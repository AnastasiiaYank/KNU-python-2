class TraceMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                attrs[attr_name] = cls.trace(attr_name)(attr_value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def trace(name):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"Calling {name} with args={args} kwargs={kwargs}")
                result = func(*args, **kwargs)
                print(f"{name} returned {result}")
                return result
            return wrapper
        return decorator


class Person(metaclass=TraceMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"{self.name} says hello!")


class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def calculate_scholarship(self):
        return self.scholarship * 2


if __name__ == '__main__':
    p = Person('John', 30)
    p.say_hello()

    s = Student('Alice', 20, 100)
    print(s.calculate_scholarship())
