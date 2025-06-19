def most_frequent(List):
    return max(set(List),key=List.count)
List=[2,1,2,2,1,3]
print(most_frequent(List))
