def get_employee_data():
    """Collect employee information and validate user input.
    Return a dictionary containing employee information."""
    employee = {}

   # Validate employee ID
    while True:
        employee_id = input("Enter employee ID: ").strip()
        if employee_id != "":
            break
        print("Error: Employee ID cannot be blank.")
   
    employee["id"] = employee_id

    # Validate employee name
    while True:
        name = input("Enter employee name: ").strip()
        if name != "":
            break
        print("Error: Name cannot be blank.")

    # Validate hours worked
    while True:
        try:
            regular_hours = float(input("Enter regular hours: "))
            if regular_hours >= 0:
                break
            print("Error: Hours worked cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

    # Validate hourly rate
    while True:
        try:
            hourly_rate = float(input("Enter hourly rate: "))
            if hourly_rate >= 0:
                break
            print("Error: Hourly rate cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

    employee["name"] = name
    employee["regular_hours"] = regular_hours
    employee["hourly_rate"] = hourly_rate

    # Validate overtime hours
    while True:
        try:
            overtime_hours = float(input("Enter overtime hours: "))
            if overtime_hours >= 0:
                break
            print("Error: Overtime hours cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

    employee["overtime_hours"] = overtime_hours
   
    # Validate federal tax percentage
    while True:
        try:
            federal_tax = float(input("Enter Federal tax percentage: "))
            if federal_tax >= 0:
                break
            print("Error: Federal tax percentage cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

    employee["federal_tax"] = federal_tax

    # Validate state tax percentage
    while True:
        try:
            state_tax = float(input("Enter State tax percentage: "))
            if state_tax >= 0:
                break
            print("Error: State tax percentage cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

    employee["state_tax"] = state_tax   

    # Validate insurance deductions
    while True:
        try:
            insurance = float(input("Enter Insurance Deductions: "))
            if insurance >= 0:
                break
            print("Error: Insurance deductions cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

    employee["insurance"] = insurance

    # Validate retirement deductions
    while True:
        try:
            retirement = float(input("Enter Retirement Deduction: "))
            if retirement >= 0:
                break
            print("Error: Retirement deduction cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

    employee["retirement"] = retirement
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

def save_report(employee, results):
    """Append payroll information to a text file."""

    with open("payroll_report.txt", "a") as file:

        file.write("Payroll Report\n")
        file.write("-" * 40 + "\n")

        file.write(f"Employee ID: {employee['id']}\n")
        file.write(f"Employee Name: {employee['name']}\n")
        file.write(f"Regular Hours: {employee['regular_hours']}\n")
        file.write(f"Overtime Hours: {employee['overtime_hours']}\n")
        file.write(f"Hourly Rate: {employee['hourly_rate']}\n")

        file.write(f"Gross Pay: {results['gross_pay']:.2f}\n")
        file.write(f"Total Deductions: {results['total_deductions']:.2f}\n")
        file.write(f"Net Pay: {results['net_pay']:.2f}\n")

    print("\nPayroll report appended to payroll_report.txt")

def display_payroll_statistics(all_results):
    """Display payroll statistics for all employees processed."""

    employee_count = len(all_results)

    total_gross_pay = 0
    total_deductions = 0
    total_net_pay = 0

    for results in all_results:
        total_gross_pay += results["gross_pay"]
        total_deductions += results["total_deductions"]
        total_net_pay += results["net_pay"]

    average_gross_pay = total_gross_pay / employee_count
    average_net_pay = total_net_pay / employee_count

    print("\nPayroll Statistics Summary")
    print("-" * 40)
    print(f"Employees Processed: {employee_count}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Total Deductions: ${total_deductions:.2f}")
    print(f"Total Net Pay: {total_net_pay:.2f}")
    print(f"Average Gross Pay: ${average_gross_pay:.2f}")
    print(f"Average Net Pay: ${average_net_pay:.2f}")
    print()
    print("End of Payroll Statistics Summary")

def initialize_report_file():
    """Gives the user the option to clear the report file."""

    while True:
        response = input(
            "Start a new payroll file? (yes/no): "
        ).strip().lower()

        if response == "yes" or response == "y":
            open("payroll_report.txt", "w").close()
            print("Payroll report file has been cleared.")
            break
        elif response == "no" or response == "n":
            print("Existing payroll report file will be used.")
            break
        else:
            print("Error: Please enter yes or no.")

def main():
    all_results = []
   
    while True:
        initialize_report_file()
        employee = get_employee_data()
        results = calculate_payroll(employee)

        display_summary(employee, results)
        save_report(employee, results)

        all_results.append(results)

        while True:
            another_employee = input(
                "\nWould you like to enter another employee?"
                " (yes/no): "
            ).strip().lower()

            if another_employee == "yes" or another_employee == "y":
                break

            if another_employee == "no" or another_employee == "n":
                display_payroll_statistics(all_results)
                return
            print("Error: Please enter yes or no.")

main()
