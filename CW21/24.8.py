import tkinter as tk
from tkinter import messagebox


class VectorInput(tk.Toplevel):
    def __init__(self, parent, n):
        super().__init__(parent)
        self.title("Enter Vector")
        self.n = n
        self.components = []
        self.entry_vars = []
        self.entry_widgets = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(self.n):
            var = tk.StringVar()
            entry = tk.Entry(self, textvariable=var)
            entry.grid(row=i, column=0)
            self.entry_vars.append(var)
            self.entry_widgets.append(entry)
        button = tk.Button(self, text="Submit", command=self.submit)
        button.grid(row=self.n, column=0)

    def submit(self):
        for var in self.entry_vars:
            if not var.get():
                tk.messagebox.showerror(
                    "Error", "All fields must be filled in.")
                return
            self.components.append(float(var.get()))
        self.destroy()


class VectorCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vector Calculator")
        self.create_widgets()

    def create_widgets(self):
        n_label = tk.Label(self, text="n:")
        n_label.grid(row=0, column=0)
        self.n_var = tk.StringVar()
        n_entry = tk.Entry(self, textvariable=self.n_var)
        n_entry.grid(row=0, column=1)

        a_label = tk.Label(self, text="a:")
        a_label.grid(row=1, column=0)
        self.a_var = tk.StringVar()
        a_entry = tk.Entry(self, textvariable=self.a_var)
        a_entry.grid(row=1, column=1)

        b_label = tk.Label(self, text="b:")
        b_label.grid(row=2, column=0)
        self.b_var = tk.StringVar()
        b_entry = tk.Entry(self, textvariable=self.b_var)
        b_entry.grid(row=2, column=1)

        enter_vector_button = tk.Button(
            self, text="Enter Vector", command=self.enter_vector)
        enter_vector_button.grid(row=3, column=0)

        self.vector_listbox = tk.Listbox(self)
        self.vector_listbox.grid(row=4, column=0, columnspan=2)

        calculate_button = tk.Button(
            self, text="Calculate", command=self.calculate)
        calculate_button.grid(row=5, column=0)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=5, column=1)

    def enter_vector(self):
        n = int(self.n_var.get())
        vector_input = VectorInput(self, n)
        self.wait_window(vector_input)
        self.vector_listbox.delete(0, tk.END)
        for component in vector_input.components:
            self.vector_listbox.insert(tk.END, component)

    def calculate(self):
        a = float(self.a_var.get())
        b = float(self.b_var.get())
        vector = [float(self.vector_listbox.get(i))
                  for i in range(self.vector_listbox.size())]
        count = sum([1 for component in vector if a <= component <= b])
        self.result_label.config(
            text=f"{count} components belong to the segment [{a}, {b}].")


if __name__ == "__main__":
    app = VectorCalculator()
    app.mainloop()

        
class VectorCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vector Calculator")
        self.create_widgets()

    def create_widgets(self):
        n_label = tk.Label(self, text="n:")
        n_label.grid(row=0, column=0)
        self.n_var = tk.StringVar()
        n_entry = tk.Entry(self, textvariable=self.n_var)
        n_entry.grid(row=0, column=1)

        a_label = tk.Label(self, text="a:")
        a_label.grid(row=1, column=0)
        self.a_var = tk.StringVar()
        a_entry = tk.Entry(self, textvariable=self.a_var)
        a_entry.grid(row=1, column=1)

        b_label = tk.Label(self, text="b:")
        b_label.grid(row=2, column=0)
        self.b_var = tk.StringVar()
        b_entry = tk.Entry(self, textvariable=self.b_var)
        b_entry.grid(row=2, column=1)

        enter_vector_button = tk.Button(
            self, text="Enter Vector", command=self.enter_vector)
        enter_vector_button.grid(row=3, column=0)

        self.vector_listbox = tk.Listbox(self)
        self.vector_listbox.grid(row=4, column=0, columnspan=2)

        calculate_button = tk.Button(
            self, text="Calculate", command=self.calculate)
        calculate_button.grid(row=5, column=0)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=5, column=1)

    def enter_vector(self):
        n = int(self.n_var.get())
        vector_input = VectorInput(self, n)
        self.wait_window(vector_input)
        self.vector_listbox.delete(0, tk.END)
        for component in vector_input.components:
            self.vector_listbox.insert(tk.END, component)

    def calculate(self):
        a = float(self.a_var.get())
        b = float(self.b_var.get())
        vector = [float(self.vector_listbox.get(i))
                  for i in range(self.vector_listbox.size())]
        count = sum([1 for component in vector if a <= component <= b])
        self.result_label.config(
            text=f"{count} components belong to the segment [{a}, {b}].")

