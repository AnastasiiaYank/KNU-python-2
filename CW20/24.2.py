import tkinter as tk


def is_palindrome(s):
    """
    Перевіряє, чи є рядок s паліндромом.
    """
    return s == s[::-1]


def check_palindrome():
    """
    Обробляє подію натискання кнопки перевірки паліндрома.
    """
    s = entry.get()
    if is_palindrome(s):
        result_label.config(text="Рядок є паліндромом")
    else:
        result_label.config(text="Рядок не є паліндромом")


# Створення вікна
window = tk.Tk()
window.title("Перевірка паліндрома")

# Створення елементів інтерфейсу
label = tk.Label(window, text="Введіть рядок:")
label.pack()

entry = tk.Entry(window)
entry.pack()

check_button = tk.Button(window, text="Перевірити", command=check_palindrome)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Запуск головного циклу програми
window.mainloop()
