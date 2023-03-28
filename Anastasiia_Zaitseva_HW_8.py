class Deque:
    def __init__(self):
        self._deque = []

    def is_empty(self):
        return len(self._deque) == 0

    def add_to_start(self, element):
        self._deque.insert(0, element)

    def add_to_end(self, element):
        self._deque.append(element)

    def take_from_start(self):
        return self._deque.pop(0)

    def take_from_end(self):
        return self._deque.pop()


def copy_deque(deque):
    elements = []
    while not deque.is_empty():
        elements.append(deque.take_from_start())
    new_deque = Deque()
    for element in elements:
        new_deque.add_to_end(element)
        deque.add_to_end(element)
    return new_deque


def calculate_length(deque):
    length = 0
    elements = []
    while not deque.is_empty():
        elements.append(deque.take_from_start())
        length += 1
    for element in elements:
        deque.add_to_end(element)
    return length
