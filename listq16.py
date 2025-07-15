#Exercise 16: Flatten Nested List
def flatten1(nested_list):
    return [item for sublist in nested_list for item in sublist]

list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
print(f"Original nested list: {list_of_lists}")
flattened_result_comp=flatten1(list_of_lists)
print(flattened_result_comp)
