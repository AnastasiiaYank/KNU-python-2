f = open('phones.txt', 'r')
data = f.readlines()
f.close()

phones = {}
for line in data:
    line = line.strip()
    line = line.split()
    name = ' '.join(line[:-1])
    phone = line[-1]
    phones[name] = phone


def find_phone(name):
    return phones[name]
