import json
from pathlib import Path

input_file = Path(__file__).with_name("employee_list.json")

with input_file.open("r", encoding="utf-8") as file:
    employeedata = json.load(file)

if employeedata:
    print("Employee data loaded successfully")
else:
    print("No employee data found")

for employee in employeedata:
    print("Employee ID:", employee["employeeid"])
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Annual Salary:", employee["annualsalary"])
    print("")