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

## Phase 3: Save the report to a file
In this next phase I created a new function called save_report.  This functions receives information from the employee dictionary and the results dictionary.  A added a docstring to describe the purpose of the function.  The next line opens the file which creates a file called payroll_report.txt and I have coded the write mode, which tells the program to erase the old contents and replace with the new contents. 

The with part of the code allows the Python program to close the file when finished.  I then added the report title and put in the \n which tells the program to start a new line. I also added a separator line with - just to make output look a little easier to read. 

I then have the program writing the employee information to the file.  The code first has what I want written to the file in the "", then it tells the program where the value should come from which is either the employee or the results functions above.  I added the .f to format the return number to 2 decimal places and then finally the \n to start a new line. 

Finally I put in a confirmation message so the user knows that the file was created successfully.  

The last piece was to update main().  I had to add the save_report to the main fuction so it actually starts the function, which creates the file and writes the payroll report. 

## Phase 4: Optional program enhancements
I wanted to see if I could add a couple of additional items to the file once I had the initial program up and running correctly.  I decided to try and tackle three different enchancements, be able to add multiple employees, append to the file so it shows all entries and output a payroll statistics summary. I have saved these additions under a new Python program called Employeewithenhancements.py

The first change was to go to the save_report function and change the "w" to "a".  This has the program do append mode, which allows it to add each new employee to the bottom of the existing file. 

The second change is was to add the payroll statistics function.  I added a new function called display_payroll_statistics. This function will receive a list named all_results.  The list will contain one payroll-results dictionary for evey employee that has been entered. First I did an employee count to count how many payroll results are in the list.  Next, I created three accumulator values that start at 0 and will then increase each time the loop runs. The next line for results in all_results, starts a loop.  The loop will go through each employee's results in the all_results list.  Each time the loop runs, the results will represent one empoloyee's calculated payroll.  The next line adds teh current employee's gross pay to the running gross-pay total.  Then I do the same for deductions and net pay.  The next two lines of code calculate the average gross and net pay.  And finally, I have the printing code to print the results from the calculations. 

I had to then add the logic into the main function so it will actually run.  The main function starts out by running the function intialize report file, which tells the program whether to append the current file or to clear the file.  Then it creates an empty list name all_results.  The input of each employee payroll results dictionary will be put into this list.  The next part of the code while true, starts the main employee processing loop.  Due to the statment being true, the program continues processing employees until it reaches the return statement. The get_employee_date function is ran to gather the inputs to store in employee.  Then the calculate_payroll function is ran to do the calcuations and then store those in results.  The the function of display_summary is ran to display the employee's payroll summary in the terminal, which also means the individual summay should appear for every employee entered.  The save_report function is ran which adds teh employee's report to the payroll_report.txt.  Due to the save_report using the append mode, the previous employees are preserved.  The all_results.append function adds theh current employee's calculated results to the all_results list.  This is the list that the statistics function will use after the user finishes entering employees. 

The next while true starts a second validation loop.  This is coded so it makes sure the user is entering an "acceptable" answer to the "add another employee" question. The .strip removes the extra spaces and teh .lower changes the uppercase letters to lowercase. The if another_employee checks if the answer is a yes or y and if so it breaks this loop and then would go back to the outer loop to start processing another employee.  If the user enters no or n, the display_payroll_statistics function will run and the stats display will be shown.  Then the return will end the main function.  I have put some validation in the code so if the user enters anything other than yes, y, no or n, the program will display the error message and ask again.  

One of my other enhancements was to add input validation logic to the input fields.  Initially, I only had the validatio logic to a couple of the begnning fields, but quickly found that I could "break" the program pretty easily without the input validation on the entire program. 

The last enhancement I made was to allow the ability to be able to add multiple employees at once. This was done in the main function.  I have coded a another_employee in the main function to get the user response.  This asks the user if they want to enter another employee.  If the user enters yes or y, it breaks the inner loop and returns the user to the outer main loop to gather the information for the next employee.  If the user enters no or n, the program ends and goes to the display statistics function.  

## Phase 5: Final Cosmetic Enhancements for program

Renamed the file to something that is related to the project - PayrollCalculatorSystem.py

The first cosmetic change I made was to enhance the Display Summary.  The first line prints a blank line and then creates a line of 50 = signs. Then I created a new title for the program to better describe it, Payroll Calculator System.  Then I added another border to the program to create a visual separation.  The program then displays the Employee ID and Employee Name.  Another blank line and border seperator was then added to create another visual separation.  I added a Pay Breakdown header so the pay stands out.  Then it puts in the pay fields of Regular Pay, Overtime Pay and Gross Pay.  Another header was added for Deductions, followed by the deduction listings of Federal Tax, State Tax, Insurance and Retirement.  Another divider line was added to separate the total deductions and net pay and then a final border to end the report.  I think these small changes enhance the readibility of the payroll summary. 

The second cosmetic change is to add a Welcome Screen to the program.  I started out by adding a border of 60 equal signs to make it look professional.  Then I added the application title to tell the audience what the program does. Then another border to continue the professional look. I added my name and the project title.  I added a blank line to create some spacing. Then I added three lines to explain the features of the program that will be shown in the demo. 

The third cosmetic change that I added was to add in a processing message for the user to see.  The first message I added says Processing employee payroll record, then it is followed by a message that says Payroll Calculation complete.  This lets the user know that the program is doing something in the background.  When I ran the program with these message the first time, there was no delay so the message got lost in the program and really didn't make sense.  I then added a delay to the messages so they now stand out and make sense when watching the program run. I also added a success message to the processing so the user will know that the employee has successfully been saved.  

The fourth cosmetic change that I made was to enhance the Payroll Statistics Summary.  The first line prints a blank line and then creates a line of 50 = signs. Then I capitalized the title for the report to better make it stand out.  Then I added another border to the program to create a visual separation.  The program then displays the total statistics before getting into the averages.  Another blank line was then added to create another visual separation.  Then it does the output for the averages.  Another divider line was added to separate to end the report with message to show the end of the payroll statistics. I think these small changes enhance the readibility of the payroll statistics. 