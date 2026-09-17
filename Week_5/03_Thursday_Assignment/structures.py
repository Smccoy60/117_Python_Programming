class Employee: 
    def __init__(self, employee_id, name, department, salary, active):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.active = active

csv_style = "10012,James,Payroll,50000,yes"
json_style = {
    "employee_id": 10012,
    "name": "James",
    "department": "Payroll",
    "salary": 50000,
    "active": "yes"
}

object_style = Employee(10012, "James", "Payroll", 50000, "yes")

print("CSV")
print(csv_style)

print("\nJSON")
print(json_style)

print("\nObject")
print(object_style.employee_id, "-", object_style.name, "-", object_style.department, "-", object_style.salary, "-", object_style.active)

