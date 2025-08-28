import json
def write_json(new_data,filename="data.json"):
    with open(filename,"r+") as file:
        file_data=json.load(file)
        file_data["emp_details"].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent=4)

new_employee = {
    "emp_name": "Nikhil",
    "email": "nikhil@geeksforgeeks.org",
    "job_profile": "Full Time"
}
write_json(new_employee)
