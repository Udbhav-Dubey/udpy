'''Exercise 16: Count Unique Words
Write a code to count the number of unique words in the given a sentence.'''
sentence = "dog is a simple animal dogs is selfless animal"
words=sentence.lower().split()
unique_words=set(words)
unique_words_count=len(unique_words)
print(unique_words)
