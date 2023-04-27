import tkinter as tk


def get_unique_words():
    # Отримуємо введений рядок з текстового поля
    input_str = input_text.get("1.0", "end-1c")

    # Розділяємо рядок на слова та видаляємо зайві символи
    words = input_str.split()
    words = [word.strip(",.?!") for word in words]

    # Отримуємо унікальні слова та сортуємо їх
    unique_words = sorted(set(words))

    # Виводимо унікальні слова у віджет список
    output_list.delete(0, tk.END)
    for word in unique_words:
        output_list.insert(tk.END, word)


# Створюємо головне вікно програми
root = tk.Tk()
root.title("Унікальні слова")

# Створюємо текстове поле для введення рядка
input_text = tk.Text(root, height=5)
input_text.pack()

# Створюємо кнопку для запуску обробки рядка
process_button = tk.Button(root, text="Обробити", command=get_unique_words)
process_button.pack()

# Створюємо віджет список для виведення унікальних слів
output_list = tk.Listbox(root)
output_list.pack()

# Запускаємо головний цикл програми
root.mainloop()
