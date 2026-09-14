from pathlib import Path

input_file = Path(__file__).with_name("Employee_Hire_Dates.txt")

with input_file.open("r", encoding="utf-8") as file:
    contents = file.read()

print("Contents of the file: ", input_file.name)
print(contents)
