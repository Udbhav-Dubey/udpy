def most_freq(List):
    counter=0
    num=List[0]
    for i in List:
        curr_frequency=List.count(i)
        if (curr_frequency>counter):
            counter=curr_frequency
            num=i

    return num

List=[2,1,2,2,1,3]
print(most_freq(List))
