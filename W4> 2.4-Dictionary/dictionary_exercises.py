# ============================================
# DICTIONARY EXERCISES
# ============================================


# ============================================
# 1a. Create a dictionary with 10 elements
# ============================================

my_dict = {
    "Name": "John Smith",
    "Age": 20,
    "Major": "Engineering",
    "College": "San Diego City College",
    "City": "San Diego",
    "State": "California",
    "Country": "USA",
    "Year": 2026,
    "Student": True,
    "GPA": 3.5,
}

print("1a. Dictionary with 10 elements:")
print(my_dict)
print()


# ============================================
# 1b. Take user input and add it to a dictionary
# ============================================

my_user_dict = {}

print("1b. Enter user information.")

continue_input = "Y"

while continue_input.upper() == "Y":
    ssn = input("SSN: ")
    name = input("Name: ")

    my_user_dict[ssn] = name

    continue_input = input("Do you want to continue (Y/N): ")

print("\nUser Dictionary:")
print(my_user_dict)
print()


# ============================================
# Converting tuples into a dictionary
# ============================================

a = [("a", 1), ("b", 2), ("c", 3)]

res = dict(a)

print("Converting tuples into a dictionary:")
print(res)
print()


# ============================================
# 1c. Check valid key/value pairs
# and check for duplicate keys
# ============================================

data = [
    ("Name", "Sarah Connor"),
    ("Date of birth", "1 Jan 1980"),
    ("Address", "1000 Black Mountain Drive", 92126),
    ("Name", "Jim Hawkins"),
]

my_valid_dict = {}

print("1c. Checking key/value pairs:")

for item in data:
    # Check if the tuple has exactly two values.
    if len(item) != 2:
        print("Error:", item, "must contain exactly one key and one value.")

        # Correct the Address entry by combining its two value fields.
        if item[0] == "Address":
            print("Correction: The address entry has too many values.")
            corrected_value = item[1] + ", " + str(item[2])
            my_valid_dict[item[0]] = corrected_value
    else:
        key = item[0]
        value = item[1]

        # Check for duplicate keys.
        if key in my_valid_dict:
            print("Duplicate key found:", key)

            new_key = input(
                "Please enter a different key for " + str(value) + ": "
            )

            while new_key in my_valid_dict:
                new_key = input("That key already exists. Enter another key: ")

            my_valid_dict[new_key] = value
        else:
            my_valid_dict[key] = value

print("\nCorrected dictionary:")
print(my_valid_dict)
print()


# ============================================
# 1d. Convert a list into a dictionary
# using a loop
# ============================================

my_list = [
    ["Name", "Alex"],
    ["Age", 20],
    ["Major", "Engineering"],
    ["City", "San Diego"],
    ["State", "California"],
]

my_list_dict = {}

for item in my_list:
    my_list_dict[item[0]] = item[1]

print("1d. List converted into dictionary:")
print(my_list_dict)
print()


# ============================================
# 1e. Count the number of words using a dictionary
# The and the count as different words
# ============================================

text = """The tiger (Panthera tigris) is a large cat and a member of the genus Panthera native to Asia. It has a powerful, muscular body with a large head and paws, a long tail and orange fur with black, mostly vertical stripes. It is traditionally classified into nine recent subspecies, though some recognise only two subspecies, mainland Asian tigers and the island tigers of the Sunda Islands."""

# Remove common punctuation.
punctuation = ".,()"

for character in punctuation:
    text = text.replace(character, "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print("1e. Word count:")
print(word_count)
print()

print("Total number of words:", len(words))
print()


# ============================================
# 2. Troubleshooting
# ============================================

d_orig = {123: "Coconut"}
d_copy = d_orig

print("Original dictionary:")
print(d_orig)

print("Copied dictionary:")
print(d_copy)
print()


# ============================================
# 2a. Change d_copy without affecting d_orig
# ============================================

d_orig = {123: "Coconut"}

# Make a separate copy of the dictionary.
d_copy = d_orig.copy()

# Change d_copy.
d_copy[123] = "Apple"

print("2a. After changing d_copy:")
print("d_orig:", d_orig)
print("d_copy:", d_copy)
print()


# ============================================
# 2b. Solve the problem using copy()
# ============================================

d_orig = {123: "Coconut"}

# copy() creates a separate dictionary.
d_copy = d_orig.copy()

d_copy[456] = "Banana"

print("2b. Using copy():")
print("d_orig:", d_orig)
print("d_copy:", d_copy)
print()


# ============================================
# 2c. Generate TypeError:
# unhashable type: 'list'
# ============================================

print("2c. Demonstrating the unhashable list error:")

# Lists cannot be used as dictionary keys because lists are mutable.
# This line is intentionally incorrect and will generate:
# TypeError: unhashable type: 'list'
# bad_dictionary = {[1, 2, 3]: "Example"}

print("A list cannot be used as a dictionary key.")
print("Dictionary keys must be hashable.")
print("For example, use a tuple instead of a list:")
print({(1, 2, 3): "Example"})
