#Exercise 15: Get the key of a minimum value
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sample_dict,key=sample_dict.get))
