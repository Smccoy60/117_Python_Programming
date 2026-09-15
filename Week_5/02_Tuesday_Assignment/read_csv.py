import csv
from pathlib import Path

input_file = Path(__file__).with_name("employee_info.csv")

total_employees = 0
total_annual_salary = 0

with input_file.open("r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Active"] == "yes":
            total_employees += 1
            total_annual_salary += int(row["AnnualSalary"])

print(f"Total active employees: {total_employees}")
print(f"Total annual salary of active employees: {total_annual_salary}")

