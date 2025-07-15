#Exercise 7: Count Occurrences

sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
from collections import Counter
dic=Counter(sports)
print(dic)
print(dic['Football'])

football_count = sports.count('Football')
print("Count:", football_count)
