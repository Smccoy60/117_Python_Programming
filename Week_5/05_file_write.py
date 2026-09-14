from pathlib import Path

output_file = Path(__file__).with_name("Employee Names.txt")

employee_names = [
    "James Smith",
    "John Doe",
    "Jane Smith",
    "Alice Johnson",
]

with output_file.open("w", encoding="utf-8") as file:
    for name in employee_names:
        file.write(name + "\n")

print("Employee names have been written to the file: ", output_file)