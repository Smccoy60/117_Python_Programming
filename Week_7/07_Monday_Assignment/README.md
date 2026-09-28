Capstone Framing Worksheet:

Project Name: Payroll Calculator and Payroll Report Generator

Purpose:
The purpose of this project is to help payroll calcualte employee pay and a generate payroll summary report. The program will collect employee payroll information, calculate gross pay, deductions, and net pay, then generate a report showing payroll results for one or more employees. 

This project demonstrates Python skills inculding data validation, calculations, file handling, report generation, and basic data analysis. 

Inputs: 
The program will require: Employee ID, Employee Name, Hourly Pay Rate, Hours Worked, Overtime Hours, Federal Tax Percentage, State Tax Percentage, Insurance Deduction, Retirement Deduction. 

In the future, it could also include Multiple employees from a CSV file, Stipend pay amounts or additional deductions.

Outputs: 
This program should produce: Gross Pay, Tax Withholdings, Total Deductions, Net Pay, and Individual Employee Payroll Summary.

An example could look like this:
Employee: Sam Smith
Gross Pay: $1000.00
Taxes: $300.00
Deductions: $200.00
Net Pay: $500.00

Constraints: 
The project will have the following limitations:
Use simplified payroll calculations for demonstration purposes
Won't perform official state or federal tax calculations
Limited to information entered by the user
Must validate user input before performing calculations
Must handle missing or incorrect data without the program crashing
Payroll calculations must be accurate based on the formulas

Likely Structure:
Main Menu.py - provides the options to add employee data, calculate payroll, view payroll summary, generate and save reports
employee.py -- stores the employee information using: classes, lists, and dictionaries
payroll calculation.py -- contains the functions to: calculate gross pay, calculate taxes, calculate deductions, and calculate net pay
report.py -- this will have the functions to: generate payroll report and save the report to a file

Risks: 
Potential challenges may include:
Determining the best file format for storing payroll data
Creating accurate payroll calculations
Manage user input errors
Determine the best structure for handling multiple employees
Format payroll report clearly
Deciding whether classes or dictionaries are better for employee data

AI Use Boundaries: 
AI can help me with: explaining Python concepts, debugging code, suggesting program structure, reviewing code for errors and recommend improvements
AI cannot help me with: project requirements, business rules, payroll formulas, program design decisions and testing and validating the program