'''Exercise 14: Filter Tuples
Write a code to filter out students with scores less than 90 from a given a list of tuples'''
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
print(f"Original student list: {students}")
high=[student for student in students if student[1]>=90]
print(high)
