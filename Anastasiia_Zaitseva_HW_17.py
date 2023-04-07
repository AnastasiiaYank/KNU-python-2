
class SeqTxt:
    def __init__(self, seq):
        self.seq = seq

    def to_text(self):
        return ' '.join(str(x) for x in self.seq)

    def to_seq(self, text):
        return [float(x) for x in text.split()]


class TxtList(list, SeqTxt):
    def __init__(self, seq):
        SeqTxt.__init__(self, seq)
        list.__init__(self, seq)


class TxtVector(SeqTxt):
    def __init__(self, seq):
        SeqTxt.__init__(self, seq)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(self.to_text())

    def load(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
        self.seq = self.to_seq(text)


class TxtMatrix(SeqTxt):
    def __init__(self, matrix):
        SeqTxt.__init__(self, matrix)
        self.vectors = [TxtVector(row) for row in matrix]

    def save(self, filename):
        with open(filename, 'w') as f:
            for vector in self.vectors:
                f.write(vector.to_text() + '\n')

    def load(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        self.vectors = [TxtVector(line.strip().split()) for line in lines]
        self.seq = [vector.seq for vector in self.vectors]

    def dot_product(self, vector):
        result = []
        for row in self.seq:
            dot = sum(float(x) * y for x, y in zip(row, vector.seq))
            result.append(dot)
        return TxtVector(result)


# a) створити два текстових файла в яких містяться два вектори однакового розміру. Обчислити їх скалярний добуток.
vector1 = TxtVector([1, 2, 3])
vector2 = TxtVector([4, 5, 6])
vector1.save('vector1.txt')
vector2.save('vector2.txt')
with open('vector1.txt', 'r') as f:
    text1 = f.read()
with open('vector2.txt', 'r') as f:
    text2 = f.read()
vector1_seq = vector1.to_seq(text1)
vector2_seq = vector2.to_seq(text2)
dot_product = sum(x * y for x, y in zip(vector1_seq, vector2_seq))
print('Scalar product of vector1 and vector2:', dot_product)

# б) створити два текстових файла в яких містяться вектор та матриця. Обчислити добуток вектору на матрицю та зберегти у новому текстовому файлі.
vector = TxtVector([1, 2, 3])
matrix = TxtMatrix([[4, 5, 6], [7, 8, 9], [10, 11, 12]])
vector.save('vector.txt')
matrix.save('matrix.txt')
with open('vector.txt', 'r') as f:
    text = f.read()
vector_seq = vector.to_seq(text)
with open('matrix.txt', 'r') as f:
    text = f.read()
matrix.load('matrix.txt')
result = matrix.dot_product(TxtVector(vector_seq))
result.save('result.txt')

# в) створити два текстових файла містяться вектор та матриця. Обчислити добуток матриці на вектор та зберегти у новому текстовому файлі.
vector = TxtVector([1, 2, 3])
matrix = TxtMatrix([[4, 5, 6], [7, 8, 9], [10, 11, 12]])
vector.save('vector.txt')
matrix.save('matrix.txt')
with open('vector.txt', 'r') as f:
    text = f.read()
vector_seq = vector.to_seq(text)
with open('matrix.txt', 'r') as f:
    text = f.read()
matrix.load('matrix.txt')
result = matrix.dot_product(TxtVector(vector_seq))
result.save('result.txt')

# г) створити два текстових файла містяться дві матриці. Обчислити їх добуток та зберегти у новому текстовому файлі.
matrix1 = TxtMatrix([[1, 2], [3, 4]])
matrix2 = TxtMatrix([[5, 6], [7, 8]])
matrix1.save('matrix1.txt')
matrix2.save('matrix2.txt')
with open('matrix1.txt', 'r') as f:
    text1 = f.read()
with open('matrix2.txt', 'r') as f:
    text2 = f.read()
matrix1.load('matrix1.txt')
matrix2.load('matrix2.txt')
result = []
for i in range(len(matrix1.seq)):
    row = []
    for j in range(len(matrix2.seq[0])):
        dot = sum(float(x) * float(y) for x, y in zip(matrix1.seq[i], [row[j] for row in matrix2.seq]))
        row.append(dot)
    result.append(row)
matrix_result = TxtMatrix(result)
matrix_result.save('matrix_result.txt')
