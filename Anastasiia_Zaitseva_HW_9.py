class Polynomial:
    def __init__(self, coeffs):  # Ініціалізує новий поліном з заданими коефіцієнтами.
        self.coeffs = coeffs

    def __str__(self):  # Повертає рядкове представлення полінома.
        terms = []
        for i, coeff in enumerate(self.coeffs):
            if coeff != 0:
                if i == 0:
                    terms.append(str(coeff))
                elif i == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{i}")
        return " + ".join(terms)

    def __getitem__(self, i):  # Повертає i-й коефіцієнт полінома.
        return self.coeffs[i]

    def __setitem__(self, i, value):  # Встановлює i-й коефіцієнт полінома в задане значення.
        self.coeffs[i] = value

    def __len__(self):  # Повертає степінь полінома.
        return len(self.coeffs)

    def __add__(self, other):  # Повертає суму двох поліномів.
        if len(self) > len(other):
            result = self.coeffs[:]
            for i in range(len(other)):
                result[i] += other[i]
        else:
            result = other.coeffs[:]
            for i in range(len(self)):
                result[i] += self[i]
        return Polynomial(result)

    def __sub__(self, other):  # Повертає різницю двох многочленів.
        if len(self) > len(other):
            result = self.coeffs[:]
            for i in range(len(other)):
                result[i] -= other[i]
        else:
            result = [-c for c in other.coeffs]
            for i in range(len(self)):
                result[i] += self[i]
        return Polynomial(result)

    def __mul__(self, other):  # Повертає добуток двох многочленів.
        result = [0] * (len(self) + len(other) - 1)
        for i in range(len(self)):
            for j in range(len(other)):
                result[i + j] += self[i] * other[j]
        return Polynomial(result)

    def evaluate(self, x):  # Обчислює многочлен у заданій точці x.
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x ** i)
        return result

    def derivative(self):  # Повертає похідну многочлена.
        result = [0] * (len(self) - 1)
        for i in range(1, len(self)):
            result[i - 1] = i * self[i]
        return Polynomial(result)


class PolynomialError(Exception):
    pass


def parse_polynomial(s):
    coeffs = {}
    for term in s.split("+"):
        term = term.strip()
        if not term:
            continue
        if "*" in term:
            coeff, var = term.split("*")
            coeff = float(coeff.strip())
            var = var.strip()
        else:
            coeff = float(term)
            var = ""
        if var:
            if "^" in var:
                var, degree = var.split("^")
                degree = int(degree)
            else:
                degree = 1
            if degree < 0:
                raise PolynomialError("Degree must be non-negative")
            coeffs[degree] = coeff
        else:
            coeffs[0] = coeff
    return Polynomial([coeffs.get(i, 0) for i in range(max(coeffs.keys()) + 1)])


try:
    p1 = parse_polynomial(input("Enter polynomial P1: "))
    p2 = parse_polynomial(input("Enter polynomial P2: "))
    expr = input("Enter expression: ")
    result = eval(expr, {"P1": p1, "P2": p2})
    print(f"Result: {result}")
except PolynomialError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
