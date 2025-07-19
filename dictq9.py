#Exercise 9: Modify Nested Dictionary
nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
nested_student_dict['class']['student']['name']='ross'
print(nested_student_dict)
