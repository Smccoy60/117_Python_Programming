def calculate_pay(hours, rate):
    gross_pay = hours * rate
    return gross_pay

def social_security_tax (gross_pay, ss_rate):
    social_security = gross_pay * ss_rate
    social_security_amount = social_security
    return social_security_amount

def net_pay (gross_pay, social_security):
    net_pay_amount = gross_pay - social_security
    return net_pay_amount

def pay_information (employee_name, gross_pay, social_security, net_pay):
    print("Employee:", employee_name)
    print("Gross Pay:", gross_pay)
    print("Social Security Amount:", social_security)
    print("Net Pay:", net_pay)

employee_name = "James"
gross_pay = calculate_pay(60, 23)
ss_rate = 0.0620
social_security = social_security_tax(gross_pay, ss_rate)
net_pay = net_pay(gross_pay, social_security)

pay_information(employee_name, gross_pay, social_security, net_pay)

print("")
print("EXPECTED AMOUNTS")
print("Gross Pay: 1380")
print("SS Amount: 85.56")
print("Net Pay: 1294.44")

#Checkpoint 1: Calculate gross pay
print("")
print("Calculation:", 60, "*", 23, "=", gross_pay)
print("Checkpoint 1: Actual Gross Pay:", gross_pay)

#Checkpoint 2: Calculate Social Security Amount
print("")
print("Calculation:", gross_pay, "*", ss_rate, "=", social_security)
print("Checkpoint 2: Actual Social Security Tax:", social_security)

#Checkpoint 3: Calculate Net Pay
print("")
print("Calculation:", gross_pay, "-", social_security, "=", net_pay)
print("Checkpoint 3: Actual Net Pay:", net_pay)