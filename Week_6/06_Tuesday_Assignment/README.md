Code Explanation:

I built a simulated program to bring back some employee deails such as name, gross pay, hours worked, and net pay.


I setup the first line to import my JSON file which is some employee data.  

I then put in some error messaging to make sure that the file has data/is loaded.  What I have is if the data loads then, I am printing a message that says that the data has loaded successfully.  If the data doesn't load, then I have a message that state that there was no employee data found.  I then test both scenerios by creating a copy of the json file and making it blank.  

When I had my program load this file I did get the message that there was no employee data found.  However, when I then pointed it to the json file that had employee data, the rest of the code runs and I get the print information that I was looking for which was the Employee ID, Name, Department, and Annual Salary. 
I setup the first line to setup the endpoint of the payroll file and then to do a query on emmployee ID. Then I chose the data I wanted the program to come back with which was the name, gross pay, hours worked and net pay. I defined this as choose display values which I am calling out later in the code. I just want the program to return these four items regardless of what information is in the endpoint file.

There is a simulated response of information that could come back. I entered more information than what I really want the program to come back with such as department to show that the program will only retrieve what I have coded for the return.

I finally have the program to print the information that I am requesting. I want it to print the endpoint that I defined. THen I want it to print my query which was the employee ID. Then finally to print the results I was requesting in the choose display values section of my code.

---

## Instructor comments:

- Your explanation of setting up the endpoint and query for the employee ID is clear and shows an understanding of how to structure the request for specific data.
- Your explanation of defining the display values and ensuring that only the desired information is returned demonstrates an understanding of filtering and selecting relevant data.
- Your explanation of printing the endpoint, query, and results shows that you understand how to present the retrieved information in a structured manner.
- Overall, your explanation indicates a solid understanding of how to simulate and retrieve specific employee data from an endpoint.