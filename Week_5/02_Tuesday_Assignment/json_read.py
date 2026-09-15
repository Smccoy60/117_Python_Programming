import json
from pathlib import Path

input_file = Path(__file__).with_name("employee_list.json")

with input_file.open("r", encoding="utf-8") as file:
    employeedata = json.load(file)

print("\nLoaded Employee Data: ", input_file.name)

for employee in employeedata:
    status = "Active" if employee["active"] else "Inactive"
    print(
        employee["employeeid"], "-", employee["name"], "-", employee["department"], "-", employee["annualsalary"], "-", status
    )
