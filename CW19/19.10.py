import math


def tagged_union_class(class_name, discriminator_field, fields_dict):
    fields_by_tag = {}
    for tag, fields in fields_dict.items():
        fields_by_tag[tag] = fields + (discriminator_field,)

    class TaggedUnion(tuple):
        __slots__ = ()
        index_by_tag = {tag: i for i, tag in enumerate(fields_by_tag)}

        def __new__(cls, tag, *args):
            if tag not in fields_by_tag:
                raise ValueError(f"Invalid tag: {tag}")
            if len(args) != len(fields_by_tag[tag]) - 1:
                raise TypeError(
                    f"{tag} expects {len(fields_by_tag[tag]) - 1} arguments, got {len(args)}")
            return super().__new__(cls, args + (tag,))

        def __getattr__(self, name):
            tag = self[-1]
            if tag not in fields_by_tag:
                raise AttributeError(
                    f"{class_name} instance has no attribute '{name}'")
            fields = fields_by_tag[tag]
            if name not in fields:
                raise AttributeError(
                    f"{class_name} instance has no attribute '{name}'")
            return self[fields.index(name)]

        def __setattr__(self, name, value):
            tag = self[-1]
            if tag not in fields_by_tag:
                raise AttributeError(
                    f"{class_name} instance has no attribute '{name}'")
            fields = fields_by_tag[tag]
            if name not in fields:
                raise AttributeError(
                    f"{class_name} instance has no attribute '{name}'")
            i = fields.index(name)
            args = list(self[:-1])
            args[i] = value
            new_instance = type(self)(*args, tag)
            self = new_instance

        def __repr__(self):
            tag = self[-1]
            fields = fields_by_tag[tag]
            values = ", ".join(
                f"{name}={getattr(self, name)!r}" for name in fields[:-1])
            return f"{class_name}({tag}, {values})"
    return TaggedUnion


Point = tagged_union_class("Point", "coord_system", {
    "cartesian": ("x", "y"),
    "polar": ("rho", "phi"),
})


def triangle_area(p1, p2, p3):
    a = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
    b = math.sqrt((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2)
    c = math.sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


# перевірка
p1 = Point("cartesian", 0, 0)
p2 = Point("cartesian", 3, 0)
p3 = Point("cartesian", 0, 4)
print(triangle_area(p1, p2, p3))  # 6.0

p1 = Point("polar", 1, math.pi/2)
p2 = Point("polar", 2, math.pi/4)
p3 = Point("polar", 3, math.pi/6)
print(triangle_area(p1, p2, p3))  # 0.26179938779914774 
