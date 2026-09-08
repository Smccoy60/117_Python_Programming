I am using a program that I previously created.  This should calculate the gross pay, show the amount of Social Security Tax and then print the net pay. 

The first change I made to create a bug was to add the social security tax instead of mulitply the gross pay.  The second bug I created was to take the hours minue pay rate instead of multiplying the two. 

I added an expected amount so I could verify when the total were what they should be. 
I added a checkpoint 1 for debugging which calculates the gross pay times the # of hours.  This showed me right away that my gross pay wasn't calculating correctly because it came up with $37 for Gross Pay. Since I added in my calculation, I could see that the calculation of 60 times 23 does NOT equal 37. I fixed this first bug find by finding and changing the gross minus hours to by the gross times the hours.  Reran the program to see if my first checkpoint matched my expected and it did. 

The second checkpoint is to calculate my social security tax.  I added a print line to show the calculation and can see clearly that 1380 times .062 does NOT equal 1380.062.  This shows me clearly that there is an error in some calculation there. I corrected this error by changing the calculation to gross pay times ss tax rate.

The third checkpoint shows the calculation of the net pay, which was correct.  No corrections needed for this checkpoint.

