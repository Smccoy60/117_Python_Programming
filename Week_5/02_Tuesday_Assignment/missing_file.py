from pathlib import Path

missing_file = Path(__file__).with_name("employee_list.csv")

try: 
    with missing_file.open("r", encoding="utf-8") as file:
        print("Loaded content from:", missing_file.name)
except FileNotFoundError:
    print("File not found:", missing_file.name)