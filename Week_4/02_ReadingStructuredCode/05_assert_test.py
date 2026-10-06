def net_pay(gross_pay, ssrate):
    return gross_pay - (gross_pay * ssrate)


assert net_pay(800, 0.062) == 750.4
assert net_pay(1200, 0.062) == 1125.6
assert net_pay(0, 0.062) == 0
assert net_pay(200, 0.0765) == 184.7
assert net_pay(-500, 0.062) == -469

# * Instructor comment: - Try this for a more detailed run!
print("\n ===> Instructor Additions: ")

try:
    assert net_pay(200, 0.0765) == 184.7
    print("Test 4 PASSED: net_pay(200, 0.0765) \n")
except AssertionError:
    print("Test 4 FAILED: net_pay(200, 0.0765) returned \n", net_pay(200, 0.0765))
# * End instructor comments

print("Gross Pay Calculated")
