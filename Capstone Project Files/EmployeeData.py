def get_employee_data():
    employee = {}
    employee["id"] = input("Enter employee ID: ")
    employee["name"] = input("Enter employee name: ")
    employee["hourly_rate"] = float(input("Enter hourly rate: "))
    employee["regular_hours"] = float(input("Enter regular hours: "))
    employee["overtime_hours"] = float(input("Enter overtime hours: "))
    employee["federal_tax"] = float(input("Enter Federal tax percentage: "))
    employee["state_tax"] = float(input("Enter State tax percentage: "))
    employee["insurance"] = float(input("Enter Insurance Deductions: "))
    employee["retirement"] = float(input("Enter Retirement Deduction: "))
    return employee

def calculate_payroll(employee):
    regular_pay = (employee["hourly_rate"] * employee["regular_hours"])
    overtime_pay = (employee["hourly_rate"] * employee["overtime_hours"] * 1.5)
    gross_pay = regular_pay + overtime_pay
    federal_tax_amount = (gross_pay * (employee["federal_tax"] / 100))
    state_tax_amount = (gross_pay * (employee["state_tax"] / 100))
    total_deductions = federal_tax_amount + state_tax_amount + employee["insurance"] + employee["retirement"]
    net_pay = gross_pay - total_deductions

    results = {
        "regular_pay": regular_pay,
        "overtime_pay": overtime_pay,
        "gross_pay": gross_pay,
        "federal_tax_amount": federal_tax_amount,
        "state_tax_amount": state_tax_amount,
        "total_deductions": total_deductions,
        "net_pay": net_pay
    }
    return results

def display_summary(employee, results):
    print("\nPayroll Summary")
    print("-" * 40)
    print(f"Employee ID: {employee['id']}")
    print(f"Employee Name: {employee['name']}")
    print()
    print(f"Regular Pay: {results['regular_pay']:.2f}")
    print(f"Overtime Pay: {results['overtime_pay']:.2f}")
    print(f"Gross Pay: {results['gross_pay']:.2f}")
    print(f"Federal Tax Amount: {results['federal_tax_amount']:.2f}")
    print(f"State Tax Amount: {results['state_tax_amount']:.2f}")
    print(f"Total Deductions: {results['total_deductions']:.2f}")
    print(f"Net Pay: {results['net_pay']:.2f}")

def main():
    employee = get_employee_data()
    results = calculate_payroll(employee)
    display_summary(employee, results)

main()
