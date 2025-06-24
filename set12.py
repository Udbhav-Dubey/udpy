s = {5, 3, 9, 1, 7}

sorted_s = sorted(s)

print("Minimum element: ", sorted_s[0])
print("Maximum element: ", sorted_s[-1])

s = {5, 3, 9, 1, 7}

min_val = float('inf')
max_val = float('-inf')

for ele in s:
    if ele < min_val:
        min_val = ele
    if ele > max_val:
        max_val = ele

print("Minimum element:", min_val)
print("Maximum element:", max_val)
