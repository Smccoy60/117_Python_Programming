## Code Explanation: 


## This was the first step in buidling my program. Create the employee dictionary
The first line of my code creates a function names get employee data.  This function will be called on later on in the code to be able to get the input information that will be entered by the user.  The employee {} line of my code creates an empty dictionary, so we can store the rest of the related information together.  The next 9 lines of code is what is going to gather the input from the user.  It will display to the user what it wants them to input and then collect their inputs to put into a dictionary. I don't have the float in front of the name or id becuase they are text and Python automatically stores them as strings.  Since the next seven lines of code we want the inputs to be a number, I put the word float in front of the input as it then tells Python to convert the entry into a decimal number.  The final line of this first section of code is the return.  This line of code sends the completed dictionary back to the function.  

At the end of this step, I put in two extra temp lines to make sure that the dictionary worked before proceeding.  Those lines were to call my initial function of get_employee_data and then to print the employee input information.

## This was the second step in my Python build. Create the payroll calculation function
The first line of the second step def calculate_payroll creates a function that runs when someone inputs information.  The employee dictionary for the first step gets passed into this function. The next line calculates the regular earnings.  It takes the input of hourly rate and regular hours and multiplies them together. These calculation steps have coded employee[xxx] so the take a look at the dictionary and retrieve teh value stored under the element called such as hourly rate, overtime hours, federal tax percentage, etc. 

The overtime pay calculation takes the hourly rate times the overtime hours that were entered and then multiplies it by 1.5 as most employer pay time and a half for overtime worked.  The Gross pay line adds the overtime pay and regular pay together and stores as gross_pay.  The next two lines are used to calculate the federal and state tax.  I have it dividing by 100 because when a user enters the tax percentage, I needed Python to change it into a decimal as it wouldn't recognize the number as a percent.  Total deductions is just simple to add up every deduction that was entered, which includes federal tax, state tax, insurance and retirement.  Then finally I have the net pay calculation which is taking the precalculated gross_pay minus the total_deductions. This would be the employees's final take-home pay. 

Then I created a dictionary for the results.  In step one I created the employee and in step two I an creating the results.  The final line is the return statement. This line sends the completed calculation back to the main program.  

My final code in this step was to add a temporary test code of: 
    employee = get_employee_data()
    results = calculate_payroll(employee)
    print(results)

## This was the third step in my Python build.  Display the payroll summary
The first line in the third step was to create a new function called display summary.  I called two elements inside the parentheses, employee and results because this function will need information from both of these dictionaries.  The code will be getting the employee Id and the employee name from the employee dictionary and the pay amounts from the results dictionary. 

The next line of the code is to print Payroll Summary on the top of the report.  THe \n tells the program to start a new line before printing.  The next line tells the program to print - 40 times across the report which will give the report a different look. 

The next two lines gets information from the employee dictionary that was created using the user inputs.  The f-string allows the variables to be entered directly into text.  The following code is print (), which just prints a blank line between the two different sets of information.  This is just basically to make things easier to read. 

The next seven lines of codes are to get information from the results dictionary and then print those results.  It uses the information between the '' to find that key to bring back the indicated information.  I have put the .2f in the code so that it will return the numbers and add 2 decimal places to the return results.  

## This was the fourth step in my Python build.  Code the Main Function
Now that I have all of my functions setup in these three steps, the next step is to call the functions to get everything to run.  I first setup a function that is named main, which will serve as the beginning point of the program.  The second line of this runs the get_employee_data function.  At this point the user will enter the information and then it is saved in the employee dictionary. The third line runs the calculate_payroll function.  This takes the information that was just entered into the employee dictionary and performs the payroll calculations.  This information gets stored in the results dictionary.  The fourth line runs the display_summary function.  This receives the information from the employee and results dictionaries and then prints the payroll summary to the screen. Then finally main() at the end of the code to actually run the function.  

## Phase 2: Add input Validation
I added some validation testing in my first function get_employee_data.

I also added a docstring so that I could explan what this function does. 
The first validation is to validate the employee name.  The while true start an infinite loop until a valid input is entered.  The first line prompts the user for a name.  I added the .strip to remove any extra spaces before or after the name after entered.  The if name checks whether something was entered, if the user were to just press enter the error message of Name cannot be blank would appear.  Once valid input has been entered, the loop would stop and move the next input. 

The next validation is the hours worked.  I again added a loop and the while true promp starts this validation loop. My code has the try next to let the code know that may fail.  The hours worked code line gets the user's input and then will convert it to a decimal number. The program than checks if the value entered is 0 or greater, negative numbers are not allowed and you can't work negative hours.  If the input is valid, the loop will exit and go to the next line.  If the input is not valid, it will give the user some type of error code such as hours worked cannot be negative.  If so some reason a input is entered that cannot be converted to a number, an error code will appear that asks the user to please enter a valid number. 

The next validation is the hourly rate.  This is setup up the same as the prior validation for hours worked. This will also give the same type of error messages if the invalid input is entered. 

Then finally, the program will continue on to create the dictionary, and return the data.  