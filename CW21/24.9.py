import tkinter as tk


class VectorInput(tk.Toplevel):
    def __init__(self, parent, n):
        super().__init__(parent)
        self.title("Enter Vector")
        self.components = []
        self.create_widgets(n)

    def create_widgets(self, n):
        for i in range(n):
            label = tk.Label(self, text=f"Component {i+1}:")
            label.grid(row=i, column=0)
            var = tk.StringVar()
            entry = tk.Entry(self, textvariable=var)
            entry.grid(row=i, column=1)
            self.components.append(var)

        ok_button = tk.Button(self, text="OK", command=self.ok)
        ok_button.grid(row=n, column=0, columnspan=2)

    def ok(self):
        self.destroy()


class ScalarProductCalculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        n_label = tk.Label(self, text="Enter n:")
        n_label.grid(row=0, column=0)
        self.n_var = tk.StringVar()
        n_entry = tk.Entry(self, textvariable=self.n_var)
        n_entry.grid(row=0, column=1)

        vector1_button = tk.Button(
            self, text="Enter Vector 1", command=self.enter_vector1)
        vector1_button.grid(row=1, column=0)

        vector2_button = tk.Button(
            self, text="Enter Vector 2", command=self.enter_vector2)
        vector2_button.grid(row=2, column=0)

        calculate_button = tk.Button(
            self, text="Calculate", command=self.calculate)
        calculate_button.grid(row=3, column=0)

        self.vector1_components = tk.Listbox(self)
        self.vector1_components.grid(row=1, column=1)

        self.vector2_components = tk.Listbox(self)
        self.vector2_components.grid(row=2, column=1)

        result_label = tk.Label(self, text="Result:")
        result_label.grid(row=3, column=1)
        self.result_var = tk.StringVar()
        result_entry = tk.Entry(
            self, textvariable=self.result_var, state="readonly")
        result_entry.grid(row=3, column=2)

    def enter_vector1(self):
        n = int(self.n_var.get())
        vector_input = VectorInput(self, n)
        self.wait_window(vector_input)
        components = [float(var.get()) for var in vector_input.components]
        self.vector1_components.delete(0, tk.END)
        for component in components:
            self.vector1_components.insert(tk.END, component)

    def enter_vector2(self):
        n = int(self.n_var.get())
        vector_input = VectorInput(self, n)
        self.wait_window(vector_input)
        components = [float(var.get()) for var in vector_input.components]
        self.vector2_components.delete(0, tk.END)
        for component in components:
            self.vector2_components.insert(tk.END, component)

    def calculate(self):
        vector1 = [float(self.vector1_components.get(i))
                   for i in range(int(self.n_var.get()))]
        vector2 = [float(self.vector2_components.get(i))
                   for i in range(int(self.n_var.get()))]
        result = sum([vector1[i] * vector2[i]
                     for i in range(int(self.n_var.get()))])
        self.result_var.set(result)


root = tk.Tk()
app = ScalarProductCalculator(root)
app.mainloop()
