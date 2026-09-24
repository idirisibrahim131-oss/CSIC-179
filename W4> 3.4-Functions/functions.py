# ============================================
# 1a. Unit Conversion Program Using Functions
# ============================================

CONVERSION_FACTOR = 2.35214583


def kpl_to_mpg(*values):
    return [value * CONVERSION_FACTOR for value in values]


def mpg_to_kpl(*values):
    return [value / CONVERSION_FACTOR for value in values]


print("UNIT CONVERSION PROGRAM")
print("-----------------------")
print("1. Convert KPL to MPG")
print("2. Convert MPG to KPL")

choice = input("Choose 1 or 2: ").strip()

while choice not in ("1", "2"):
    print("Error: Please enter 1 or 2.")
    choice = input("Choose 1 or 2: ").strip()

number_of_values = input(
    "How many values do you want to convert? "
).strip()

while not number_of_values.isdigit() or int(number_of_values) <= 0:
    print("Error: Please enter a positive whole number.")
    number_of_values = input(
        "How many values do you want to convert? "
    ).strip()

number_of_values = int(number_of_values)
values = []

for index in range(number_of_values):
    value = input(f"Enter value {index + 1}: ").strip()

    while True:
        try:
            number = float(value)

            if number > 0:
                values.append(number)
                break

            print("Error: Please enter a positive number greater than 0.")
        except ValueError:
            print("Error: Please enter a valid number.")

        value = input(f"Enter value {index + 1}: ").strip()

if choice == "1":
    results = kpl_to_mpg(*values)
    source_unit = "KPL"
    target_unit = "MPG"
else:
    results = mpg_to_kpl(*values)
    source_unit = "MPG"
    target_unit = "KPL"

print("\nConversion Results:")

for value, result in zip(values, results):
    print(value, source_unit, "=", round(result, 2), target_unit)


# ============================================
# 1b. Function with Any Number of Unnamed
# Arguments and Print Them in Reverse Order
# ============================================


def reverse_values(*args):
    print("\n1b. Values in reverse order:")

    for value in reversed(args):
        print(value)


reverse_values(10, 20, 30, 40, 50)


# ============================================
# 1c. Lists and Dictionaries Passed into
# Functions
# ============================================


def change_list(my_list):
    my_list.append("New Item")


my_list = ["Apple", "Banana", "Orange"]

print("\n1c. List before changing:")
print(my_list)

change_list(my_list)

print("List after changing:")
print(my_list)


def change_dictionary(my_dictionary):
    my_dictionary["Age"] = 20


my_dictionary = {
    "Name": "John",
    "Age": 19
}

print("\nDictionary before changing:")
print(my_dictionary)

change_dictionary(my_dictionary)

print("Dictionary after changing:")
print(my_dictionary)


def change_list_copy(my_list):
    new_list = my_list.copy()
    new_list.append("New Item")

    print("\nList inside function:")
    print(new_list)


original_list = ["Apple", "Banana", "Orange"]

print("\nOriginal list before function:")
print(original_list)

change_list_copy(original_list)

print("Original list after function:")
print(original_list)


def change_dictionary_copy(my_dictionary):
    new_dictionary = my_dictionary.copy()
    new_dictionary["City"] = "San Diego"

    print("\nDictionary inside function:")
    print(new_dictionary)


original_dictionary = {
    "Name": "John",
    "Age": 19
}

print("\nOriginal dictionary before function:")
print(original_dictionary)

change_dictionary_copy(original_dictionary)

print("Original dictionary after function:")
print(original_dictionary)


from copy import deepcopy


nested_list = [
    ["Apple", "Banana"],
    ["Orange", "Grape"]
]

deep_copy_list = deepcopy(nested_list)
deep_copy_list[0].append("Mango")

print("\nNested list:")
print(nested_list)

print("Deep copy:")
print(deep_copy_list)


# ============================================
# 1d. Local and Global Variables
# ============================================

x = 5


def funct_1():
    x = 3
    print("x inside funct_1():", x)


funct_1()

print("x after funct_1():", x)


def funct_2():
    global x
    x = 2


funct_2()

print("x after funct_2():", x)


# ============================================
# 2. Troubleshooting
# ============================================


def my_func(a, b, *c):
    print("\n2. Troubleshooting:")
    print("a =", a)
    print("b =", b)
    print("Additional arguments =", c)


my_func(1, 2, 3, 4, 5, 6)


# ============================================
# Troubleshooting the Global Variable
# ============================================


def my_func_global():
    global x
    x = 100


x = 10
my_func_global()

print("\nGlobal x after my_func_global():")
print(x)
