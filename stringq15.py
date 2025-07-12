#Exercise 15: Remove special symbols / punctuation from a string
import re

str1 = "Hello!!!, he said ---and went."

# Substitute anything not a-z, A-Z, 0-9 or space with ''
clean_str = re.sub(r'[^A-Za-z0-9 ]+', '', str1)

print(clean_str)

