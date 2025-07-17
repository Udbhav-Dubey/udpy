'''Exercise 1: Perform Basic Set Operations

    Create a Set: Create a set named fruits containing “apple”, “banana”, “mango”, and “orange”.
    Add Element: Add “grape” to the fruits set.
    Remove Element: Remove “banana” from the fruits set.
    Discard Element: Try to discard “mango” from the fruits set.
'''
fruits={"apple","banana","mango","orange"}
print(fruits)
fruits.add("grape")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("mango")
print(fruits)
