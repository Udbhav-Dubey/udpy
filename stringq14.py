#Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
newstr=list(filter(None,str_list))
print(newstr)
