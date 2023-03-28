class NumIterator:
    def __init__(self, str):
        self.str = str
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.str)-1:
            raise StopIteration
        if self.str[self.index] in '0123456789':
            return self.str[self.index]
        return self.__next__()


print(list(NumIterator('23otvb6qow21')))
