## Capstone Proposal Worksheet:

## Project Name: Payroll Calculator and Payroll Summary Report Generator

## Purpose:
The purpose of this project is to create a Python program that calculates and summarizes payroll information using fictional employee data.  The program will collect basid employee and payroll information, calculate regular pay, simplified tax withholdings, deductions and net pay.  It will then generate a summary and allow the user to save the summary to a file. 

This project is intended to demonstrates Python skills such as user input, data validation, calculations, functions, dictionaries, conditional statements, loops, exception handling, file handling and formatted output.  It is only a demonstration tool and will not calculate official payroll or tax amounts.  

## Inputs: 
The program will request: Employee ID, Employee Name, Hourly Pay Rate, Regular Hours Worked, Overtime Hours, Fictional Federal Tax Percentage, Fictional State Tax Percentage, Insurance Deduction, Retirement Deduction. 

In the future, it could also include Multiple employees from a CSV file, Stipend pay amounts or additional deductions.

## Outputs: 
This program should produce: Gross Pay, Tax Withholdings, Total Deductions, Net Pay, and Individual Employee Payroll Summary.

An example could look like this:
```    
Employee: Sam Smith
Gross Pay: $1000.00
Taxes: $300.00
Deductions: $200.00
Net Pay: $500.00
```

## Constraints: 
The project will have the following limitations:

* The project will use fictional information
* Calculations will be simplified for demonstration purposes
* The program will not use official federal or state tax tables
* The program will not connect to a payroll or HR system
* The program will not process live employee information
* The program will use only concepts and code that I can explain.
* The first version will use manually entered information.
* The program must handle invalid or missing input without crashing.

## Likely Structure:
The project will use a function-based structure.  Each major calculation will be handled by a separate function, including collecting input, validating numeric values, calculating payroll results, formatting the payroll summary and saving the report. 

A dictionary will likely be used to keep related employee and payroll information together.  The first version will be contained in one main Python file unless it is determined the report-saving function is better as a second file. 

This first version of the program will be developed in a single Python script file.  Maybe in the future payroll calculations and report generation can be put into separate modules. 

## Potential Function List
This project will likely contain the following functions:
* main() - which will control the program flow
* get_employee_data - which will collect the payroll information from the user
* get_valid_number - which will validate the input and then handle the invalid entries
* calculate_payroll - calculate the gross pay, taxes, deductions and net pay
* display_summary - will display a payroll summary with the given information
* save_report - this will save the payroll summary to a file

## Risks: 
Potential risks may include:
* Incorrect formulas or calculation order
* Negative or nonnumeric input
* Percentages entered in inconsistent formulas
* Deductions greater than the Gross Pay
* Difficulty in selecting the best report-file format
* Adding more features than can be completed and tested
* Using code that can be difficult to explain

## Backlog Features
After the core version works, some possible additions include:
* Process multiple employees at a time
* Import employee information from a CSV file
* Export a combined payroll report
* Add stipends or other income
* Add more deduction categories
* Separate the program into multiple modules

## AI Use Boundaries: 
AI can help me with: explaining Python concepts, debugging code, suggesting program structure, reviewing code for errors and recommend improvements

I will make the final decisions about: purpose of the project, payroll calculation rules, input and output requirements, program structure, testing and validating the program