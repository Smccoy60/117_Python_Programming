def ot_earned(hoursWorked):
    return hoursWorked > 40

print("Test OT Earned Function 1: ", ot_earned(45), " - Expected: ", True)
print("Test OT Earned Function 2: ", ot_earned(40), " - Expected: ", False)
print("Test OT Earned Function 3: ", ot_earned(39), " - Expected: ", False)