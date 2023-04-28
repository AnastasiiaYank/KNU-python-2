import tkinter as tk
import csv


class Employee:
    def __init__(self, name, personnel_number, salary, hours_per_day):
        self.name = name
        self.personnel_number = personnel_number
        self.salary = salary
        self.hours_per_day = hours_per_day
        self.timesheet = [0] * 31

    def input_timesheet(self, day, hours):
        self.timesheet[day-1] = hours

    def calculate_salary(self):
        total_hours = sum(self.timesheet)
        salary_per_hour = self.salary / (self.hours_per_day * 30)
        salary = salary_per_hour * total_hours
        return salary

    def __str__(self):
        return f"{self.name} ({self.personnel_number})"


class TimesheetWindow(tk.Toplevel):
    def __init__(self, parent, employee):
        super().__init__(parent)
        self.employee = employee
        self.title(f"Timesheet for {employee.name}")
        self.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter hours worked for each day:").pack()
        self.entries = []
        for i in range(31):
            frame = tk.Frame(self)
            frame.pack()
            day_label = tk.Label(frame, text=f"Day {i+1}:")
            day_label.pack(side=tk.LEFT)
            hours_entry = tk.Entry(frame, width=5)
            hours_entry.pack(side=tk.LEFT)
            self.entries.append(hours_entry)
        tk.Button(self, text="Save", command=self.save_timesheet).pack()

    def save_timesheet(self):
        for i, entry in enumerate(self.entries):
            hours = int(entry.get())
            self.employee.input_timesheet(i+1, hours)
        self.destroy()


class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Employee Timesheets")
        self.parent.geometry("400x400")
        self.employees = []
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="Add Employee", command=self.add_employee).pack()
        tk.Button(self, text="Enter Timesheets",
                  command=self.enter_timesheets).pack()
        tk.Button(self, text="Calculate Salaries",
                  command=self.calculate_salaries).pack()
        self.employee_listbox = tk.Listbox(self)
        self.employee_listbox.pack(fill=tk.BOTH, expand=True)
        self.load_employees()

    def add_employee(self):
        personnel_number = len(self.employees) + 1
        employee = Employee(
            f"Employee {personnel_number}", personnel_number, 2000, 8)
        self.employees.append(employee)
        self.employee_listbox.insert(tk.END, str(employee))

    def enter_timesheets(self):
        selection = self.employee_listbox.curselection()
        if len(selection) == 1:
            employee = self.employees[selection[0]]
            TimesheetWindow(self.parent, employee)

    def calculate_salaries(self):
        for employee in self.employees:
            salary = employee.calculate_salary()
            print(f"{employee.name}: {salary}")

    def load_employees(self):
        try:
            with open("employees.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    name, personnel_number, salary, hours_per_day = row
                    employee = Employee(name, int(personnel_number), float(
                        salary), int(hours_per_day))
                    timesheet = [int(hours) for hours in row[4:]]
                    employee.timesheet = timesheet
                    self.employees.append(employee)
                    self.employee_listbox.insert(tk.END, str(employee))
        except FileNotFoundError:
            pass

    def save_employees(self):
        with open("employees.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for employee in self.employees:
                row = [employee.name, employee.personnel_number,
                       employee.salary, employee.hours_per_day] + employee.timesheet
                writer.writerow(row)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
