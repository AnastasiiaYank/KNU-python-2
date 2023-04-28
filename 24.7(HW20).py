import tkinter as tk


def separate_digits(string):
    digits = ""
    non_digits = ""
    for char in string:
        if char.isdigit():
            digits += char
        else:
            non_digits += char
    return digits, non_digits


def show_results():
    string = entry.get()
    digits, non_digits = separate_digits(string)
    result1.config(text=digits)
    result2.config(text=non_digits)


# Create the main window
root = tk.Tk()
root.title("Separate Digits")

# Create the input field
label = tk.Label(root, text="Enter a string:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create the button to show the results
button = tk.Button(root, text="Show Results", command=show_results)
button.pack()

# Create the two result labels
result1 = tk.Label(root, text="")
result1.pack()
result2 = tk.Label(root, text="")
result2.pack()

# Start the main loop
root.mainloop()
