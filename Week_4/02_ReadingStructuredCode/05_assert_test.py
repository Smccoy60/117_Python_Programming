def net_pay(gross_pay, ssrate):
    return gross_pay - (gross_pay * ssrate)

assert net_pay(800, .062) == 750.4
assert net_pay(1200, .062) == 1125.6
assert net_pay(0, .062) == 0
assert net_pay(200, .0765) == 184.7
assert net_pay(-500, .062) == -469

print("Gross Pay Calculated")