"""Examples of common Python list operations."""

import copy


# a. Generate a list of 100 integers using range().
my_list = list(range(1, 101))

print("my_list:", my_list)
print("Data type:", type(my_list))

my_list.append(101)
print("After append:", my_list)

my_list.insert(0, 0)
print("After insert:", my_list)

my_list.remove(50)
print("After remove:", my_list)

my_list.reverse()
print("After reverse:", my_list)


# b. Move the last three items to the beginning.
my_list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_b = my_list_b[-3:] + my_list_b[:-3]

print("List after moving last three to beginning:", my_list_b)


# c. Result of len([[1, 2]] * 3).
result_c = len([[1, 2]] * 3)

print("Result of len([[1, 2]] * 3):", result_c)


# d. Create a list of 10 items with duplicate entries.
my_list_ten = [10, 20, 30, 20, 40, 50, 30, 60, 70, 20]
my_list_ten_mem = [id(item) for item in my_list_ten]

print("my_list_ten:", my_list_ten)
print("Memory addresses:", my_list_ten_mem)

unique_addresses = set(my_list_ten_mem)
duplicate_addresses = [
    address for address in unique_addresses if my_list_ten_mem.count(address) > 1
]

print("Unique memory addresses:", unique_addresses)
print("Duplicate memory addresses:", duplicate_addresses)


# e. Delete my_list_ten.
del my_list_ten

print("my_list_ten has been deleted.")


# f. Create a new list with the same 10 items.
my_new_list = [10, 20, 30, 20, 40, 50, 30, 60, 70, 20]
my_new_list_mem = [id(item) for item in my_new_list]

print("my_new_list:", my_new_list)
print("New memory addresses:", my_new_list_mem)
print("Memory addresses from my_list_ten_mem:", my_list_ten_mem)
print("Memory addresses from my_new_list:", my_new_list_mem)

if my_list_ten_mem == my_new_list_mem:
    print("The memory addresses are the same.")
else:
    print("The memory addresses are not exactly the same.")

print(
    "Observation: Some identical immutable objects may have the same memory address "
    "because Python can reuse objects."
)


# g. Create a copy of x without changing the original x.
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = copy.deepcopy(x)

y[0][0] = 100

print("Original x:", x)
print("Copied y:", y)


# h. Use multiple expressions in a list comprehension.
numbers = [1, 2, 3, 4, 5]
multiple_expressions = [number * 2 + 1 for number in numbers]

print("List comprehension with multiple expressions:", multiple_expressions)


# i. Count spaces using a list comprehension.
statement = "To be, or not to be, this is the question"
spaces = [character for character in statement if character == " "]

print("Number of spaces:", len(spaces))


# j. Five list operations.
list_j = [1, 2, 3]

list_j.append(4)
print("After append():", list_j)

list_j.extend([5, 6])
print("After extend():", list_j)

list_j.insert(0, 0)
print("After insert():", list_j)

list_j.remove(3)
print("After remove():", list_j)

removed_item = list_j.pop()
print("After pop():", list_j)
print("Removed item:", removed_item)
