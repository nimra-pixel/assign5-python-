# Python List Methods

# 1. append()
# Description:
# Adds a single element to the end of the list.

# Syntax:
# list.append(element)
# element: The item to be added to the list.

# Return Type:
# None (the list is modified in place).

# Example:
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)
# fruits is now ['apple', 'banana', 'orange']


# 2. extend()
# Description:
# Extends the list by appending elements from another iterable (e.g., another list, tuple, etc.).

# Syntax:
# list.extend(iterable)
# iterable: An iterable (e.g., list, tuple) whose elements are added to the list.

# Return Type:
# None (the list is modified in place).

# Example:
fruits = ['apple', 'banana']
more_fruits = ['orange', 'grape']
fruits.extend(more_fruits)
print(fruits)
# fruits is now ['apple', 'banana', 'orange', 'grape']


# 3. insert()
# Description:
# Inserts an element at a specified position in the list.

# Syntax:
# list.insert(index, element)
# index: The position where the element should be inserted.
# element: The item to be inserted.

# Return Type:
# None (the list is modified in place).

# Example:
fruits = ['apple', 'banana']
fruits.insert(1, 'orange')
print(fruits)
# fruits is now ['apple', 'orange', 'banana']


# 4. remove()
# Description:
# Removes the first occurrence of the specified element from the list.

# Syntax:
# list.remove(element)
# element: The item to be removed.

# Return Type:
# None (the list is modified in place).

# Example:
fruits = ['apple', 'banana', 'orange']
fruits.remove('banana')
print(fruits)
# fruits is now ['apple', 'orange']


# 5. pop()
# Description:
# Removes and returns the element at the specified position. If no index is specified, it removes and returns the last item.

# Syntax:
# list.pop([index])
# index: The position of the item to be removed (optional).

# Return Type:
# The removed item.

# Example:
fruits = ['apple', 'banana', 'orange']
removed_fruit = fruits.pop(1)
print(fruits)
# removed_fruit is 'banana'
# fruits is now ['apple', 'orange']


# 6. clear()
# Description:
# Removes all elements from the list, resulting in an empty list.

# Syntax:
# list.clear()

# Return Type:
# None (the list is modified in place).

# Example:
fruits = ['apple', 'banana', 'orange']
fruits.clear()
print(fruits)
# fruits is now []


# 7. index()
# Description:
# Returns the index of the first occurrence of the specified element. Raises a ValueError if the element is not found.

# Syntax:
# list.index(element, [start], [end])
# element: The item to search for.
# start: The starting position in the list to search (optional).
# end: The ending position in the list to search (optional).

# Return Type:
# The index of the first occurrence of the element.

# Example:
fruits = ['apple', 'banana', 'orange']
index = fruits.index('banana')
print(fruits)
# index is 1


# 8. count()
# Description:
# Returns the number of times the specified element appears in the list.

# Syntax:
# list.count(element)
# element: The item to count.

# Return Type:
# The count of the element.

# Example:
fruits = ['apple', 'banana', 'orange', 'banana']
count = fruits.count('banana')
print(fruits)
# count is 2


# 9. sort()
# Description:
# Sorts the list in ascending order by default. Can be customized using optional parameters.

# Syntax:
# list.sort(key=None, reverse=False)
# key: A function that serves as a key for the sort comparison (optional).
# reverse: If True, the list is sorted in descending order (optional).

# Return Type:
# None (the list is modified in place).

# Example:
fruits = ['banana', 'apple', 'orange']
fruits.sort()
print(fruits)
# fruits is now ['apple', 'banana', 'orange']

# Example with reverse:
fruits.sort(reverse=True)
print(fruits)
# fruits is now ['orange', 'banana', 'apple']


# 10. reverse()
# Description:
# Reverses the order of the list.

# Syntax:
# list.reverse()

# Return Type:
# None (the list is modified in place).

# Example:
fruits = ['apple', 'banana', 'orange']
fruits.reverse()
print(fruits)
# fruits is now ['orange', 'banana', 'apple']


# 11. copy()
# Description:
# Returns a shallow copy of the list.

# Syntax:
# list.copy()

# Return Type:
# A new list that is a shallow copy of the original list.

# Example:
fruits = ['apple', 'banana', 'orange']
new_fruits = fruits.copy()
print(fruits)
# new_fruits is ['apple', 'banana', 'orange']
