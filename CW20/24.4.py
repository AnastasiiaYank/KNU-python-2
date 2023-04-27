import tkinter as tk


def count_sign_changes():
    sequence = sequence_entry.get()  # отримуємо введену послідовність
    numbers = sequence.split()  # розділяємо послідовність на окремі числа
    sign_changes = 0
    prev_sign = None
    for num in numbers:
        num = int(num)
        if prev_sign is None:
            prev_sign = num
            continue
        if num == 0:
            break
        if num * prev_sign < 0:
            sign_changes += 1
        prev_sign = num
    sign_changes_label.config(
        text="Кількість змін знаку: {}".format(sign_changes))


# створюємо графічний інтерфейс
root = tk.Tk()
root.title("Рахуємо зміни знаку")

sequence_label = tk.Label(
    root, text="Введіть послідовність чисел (розділіть пробілами):")
sequence_label.pack()

sequence_entry = tk.Entry(root)
sequence_entry.pack()

count_button = tk.Button(root, text="Рахувати", command=count_sign_changes)
count_button.pack()

sign_changes_label = tk.Label(root, text="")
sign_changes_label.pack()

root.mainloop()
