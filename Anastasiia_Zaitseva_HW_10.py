# Define a class for working with text files
class TextFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.num_numbers = 0
        self.num_lines = 0

    # Method to enter numbers from console into file line by line
    def enter_numbers(self):
        try:
            with open(self.file_name, 'a') as f:
                while True:
                    line = input("Enter numbers separated by spaces (or 'q' to quit): ")
                    if line == 'q':
                        break
                    numbers = line.split()
                    for num in numbers:
                        try:
                            float(num)
                        except ValueError:
                            print("Invalid number entered")
                            continue
                        f.write(num + ' ')
                        self.num_numbers += 1
                    f.write('\n')
                    self.num_lines += 1
        except IOError:
            print("Error creating or writing to file")

    # Method to create a file from a two-dimensional array of numbers
    def create_file(self, arr):
        try:
            with open(self.file_name, 'w') as f:
                for row in arr:
                    for num in row:
                        f.write(str(num) + ' ')
                        self.num_numbers += 1
                    f.write('\n')
                    self.num_lines += 1
        except IOError:
            print("Error creating or writing to file")

    # Method to display the contents of the file on the console and return a given number
    def display_file(self, num):
        try:
            with open(self.file_name, 'r') as f:
                for line in f:
                    self.num_lines += 1
                    numbers = line.split()
                    for n in numbers:
                        self.num_numbers += 1
                        if float(n) == num:
                            return num
                    print(line.rstrip())
        except IOError:
            print("Error reading from file")
        return None

    # Method to add an array of numbers to the file with a newline at the end
    def add_numbers(self, arr):
        try:
            with open(self.file_name, 'a') as f:
                for num in arr:
                    try:
                        float(num)
                    except ValueError:
                        print("Invalid number entered")
                        continue
                    f.write(str(num) + ' ')
                    self.num_numbers += 1
                f.write('\n')
                self.num_lines += 1
        except IOError:
            print("Error creating or writing to file")

    # Method to delete a number at a given line number and position in the array
    def delete_number(self, line_num, pos):
        try:
            with open(self.file_name, 'r') as f:
                lines = f.readlines()
            with open(self.file_name, 'w') as f:
                for i, line in enumerate(lines):
                    if i == line_num:
                        numbers = line.split()
                        if pos >= len(numbers):
                            print("Invalid position entered")
                            return
                        del numbers[pos]
                        line = ' '.join(numbers) + '\n'
                    f.write(line)
        except IOError:
            print("Error reading from or writing to file")