#Exercise 3: Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
size=len(sample_list)
size=int(size/3)
start=0
end=size
print(sample_list[:size][::-1])
print(sample_list[size:size+3][::-1])
print(sample_list[size+3:][::-1])
