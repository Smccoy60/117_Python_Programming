I did two different tests. I did a print test first.


In this test, I wanted to program to return whether the hours entered are over the 40 hour per week threshold to determine if OT has been earned.  I did a return of hours worked greater than 40.  I tested three different values, one for sure over 40, one at exactly 40 and one under 40 to see what the results would be in these three different scenarios. 

The second test I ran was an assertion test.  Here I wanted to calculate the net pay.  I first setup the formula to take the gross pay minus the gross times the ss rate.  This will return the net pay. I did an assert to check five different scenarios. Then if everything checks out, I have it print Gross pay calculated.  I actually ran into an assert testing error at first becuase I changed the tax rate to .0765.  I got an assertion error becuase I accidentally keyed .765 instead of .0765.  I made this change in the code and ran the program again and then all passed.  I attached a screenshot of the assertion error.  
In this test, I wanted to program to return whether the hours entered are over the 40 hour per week threshold to determine if OT has been earned. I did a return of hours worked greater than 40. I tested three different values, one for sure over 40, one at exactly 40 and one under 40 to see what the results would be in these three different scenarios.

---

## Instructor comments:

- Your explanation of the print test is clear and shows a good understanding of how to verify the program's behavior for different input scenarios.
- You also demonstrated an understanding of how to test boundary conditions, such as exactly 40 hours, which is important for ensuring the correctness of overtime calculations.
- Overall, your explanation shows a solid understanding of how to read and verify structured code for different input scenarios.

- Improvement/Suggestion: I modified your 05_assert_test.py file to show you a more structured way to test your code using assertions, which can help automate the verification of different input scenarios.
