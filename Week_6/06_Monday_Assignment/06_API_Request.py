def build_request(employee_id):
    return {"endpoint": "/payroll", "query": {"employee_id": employee_id}}

def choose_display_values(response_data):
    employee = response_data["employee"]
    return {
        "name": employee["name"],
        "gross_pay": employee["gross_pay"],
        "hours_worked": employee["hours_worked"],
        "net_pay": employee["net_pay"]
    }

request_details = build_request("12345")

simulated_response = {
    "employee":{
        "employee_id": 12345,
        "name": "Steven Smith",
        "department": "Finance",
        "gross_pay": 700,
        "hours_worked": 40,
        "net_pay": 400
    }
}

selected_values = choose_display_values(simulated_response)

print("Request enpoint:", request_details["endpoint"])
print("Employee ID:", request_details["query"]["employee_id"])
print("Selected Values:", selected_values)