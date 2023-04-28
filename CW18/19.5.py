def type_check(cls):
    orig_init = cls.__init__
    field_types = getattr(cls, '_field_types', {})

    def new_init(self, *args, **kwargs):
        for arg, arg_type in zip(args, field_types.values()):
            if not isinstance(arg, arg_type):
                raise ValueError(f"Expected {arg_type}, but got {type(arg)}")
        for arg_name, arg_type in field_types.items():
            if arg_name in kwargs and not isinstance(kwargs[arg_name], arg_type):
                raise ValueError(
                    f"Expected {arg_type}, but got {type(kwargs[arg_name])}")
        orig_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@type_check
class Point:
    _field_types = {'x': int, 'y': int}

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


@type_check
class Circle:
    _field_types = {'center': Point, 'radius': float}

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def move(self, dx, dy):
        self.center.move(dx, dy)


# Raises ValueError: Expected <class 'int'>, but got <class 'str'>
p = Point(1, 2)
# Raises ValueError: Expected <class 'float'>, but got <class 'str'>
c = Circle(Point(0, 0), float(1))


p = Point(1, 2)
p.move(3, 4)
print(p.x, p.y)  # Output: 4 6

c = Circle(Point(0, 0), 1.0)
c.move(1, 2)
print(c.center.x, c.center.y, c.radius)  # Output: 1 2 1.0
