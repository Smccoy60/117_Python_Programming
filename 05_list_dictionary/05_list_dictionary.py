employee = {
    "name": "Sarah",
    "department": "Payroll",
    "hourly_rate": 27.00,
    "hours_worked": 40
}

gross_pay = employee["hourly_rate"] * employee["hours_worked"]

print("Employee Name:", employee["name"])
print("Department:", employee["department"])
print("Hourly Rate:", employee["hourly_rate"])
print("Hours Worked:", employee["hours_worked"])
print("Gross Pay:", gross_pay)