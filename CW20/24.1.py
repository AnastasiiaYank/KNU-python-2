import tkinter as tk


def calculate():
    x = float(x_entry.get())
    epsilon = float(epsilon_entry.get())
    if abs(x) >= 1:
        result_label.config(text="|x| must be less than 1")
        return
    y = 1 / (1 + x**2)
    term = y
    total = term
    n = 1
    while abs(term) >= epsilon:
        n += 1
        term *= -2 * x * (n - 1) / n
        total += term
    result_label.config(text="Result: {:.6f}".format(total))


root = tk.Tk()
root.title("Sum of Terms Calculator")

x_label = tk.Label(root, text="Enter x:")
x_label.pack()
x_entry = tk.Entry(root)
x_entry.pack()

epsilon_label = tk.Label(root, text="Enter epsilon:")
epsilon_label.pack()
epsilon_entry = tk.Entry(root)
epsilon_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
