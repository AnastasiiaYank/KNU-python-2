import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper


class Btree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    @calculate_time
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Btree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Btree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    @calculate_time
    def search(self, value):
        if value < self.value:
            if self.left is None:
                return f"{value} not found"
            return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return f"{value} not found"
            return self.right.search(value)
        else:
            return f"{value} found"


# Build the binary search tree
bst = Btree(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Search for a value
print(bst.search(60))

