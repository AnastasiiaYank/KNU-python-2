class Iter:
    def __init__(self, seq):
        self.seq = seq
        self.index = len(seq)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        if self.seq[self.index] != '':
            return self.seq[self.index]
        return self.__next__()


print(list(Iter([1, 2, 3, 4, 5, '', 7, 8, 9, 10])))
