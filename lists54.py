from collections import Counter
def most_freq(List):
    occurence=Counter(List)
    return occurence.most_common(1)[0][0]

List = [2, 1, 2, 2, 1, 3]
print(most_freq(List))
