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