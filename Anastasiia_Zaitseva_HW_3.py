# 12.10.Дано файл f,компоненти якого є цілими числами. Файл f містить   рівне   число   додатних   та   від’ємних   чисел. Використовуючи  допоміжний  файл h,  переписати  компоненти файлу f в файл g так, щоб у файлі g:
# а) не було двох сусідніх чисел одного знаку;
# б) спочатку йшли додатні, потім від’ємні числа;
# в) числа йшли таким чином: два додатних, два від’ємних і т.д. (припускається, що число компонент в файлі f ділиться на 4).

f = open('f.txt', 'r')  # 1 2 3 4 -1 -2 -3 -4
g = open('g.txt', 'w')

numbers = [float(i) for i in f.read().split()]
positive = []
negative = []
for i in numbers:
    if i >= 0:
        positive.append(i)
    else:
        negative.append(i)

# а)
a = []
for i, j in zip(positive, negative):
    a.append(i)
    a.append(j)

# б)
b = positive + negative

# в)
c = []
for i in range(0, len(positive), 2):
    c.append(positive[i])
    c.append(positive[i+1])
    c.append(negative[i])
    c.append(negative[i+1])

g.write(f'''a) {a}
b) {b}
c) {c}
''')
