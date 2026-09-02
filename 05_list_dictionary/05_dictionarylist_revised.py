employees = [
    {
        "employee_id": 1,
        "name": "Sarah",
        "department": "Payroll",
        "hourly_rate": 27.00,
        "hours_worked": 40
    },
    {
        "employee_id": 2,
        "name": "John",
        "department": "IT",
        "hourly_rate": 30.00,
        "hours_worked": 35
    },
    {
        "employee_id": 3,
        "name": "Alice",
        "department": "HR",
        "hourly_rate": 28.00,
        "hours_worked": 38
    },
    {
        "employee_id": 4,
        "name": "Bob",
        "department": "Finance",
        "hourly_rate": 32.00,
        "hours_worked": 42
    }
]

employee_id = int(input("Enter employee ID: "))
found = False

for emp in employees:
    if emp["employee_id"] == employee_id:
        found = True
        print("Employee Name:", emp["name"])
        print("Department:", emp["department"])
        print("Hourly Rate:", emp["hourly_rate"])
        print("Hours Worked:", emp["hours_worked"])

if not found:
    print("Employee not found.")
