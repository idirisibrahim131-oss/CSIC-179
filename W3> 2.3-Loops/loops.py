# ==========================================
# 1a. WHILE LOOP - COLLATZ SEQUENCE
# ==========================================

n0 = int(input("Enter a positive integer: "))

while n0 <= 0:
    print("Please enter a positive integer.")
    n0 = int(input("Enter a positive integer: "))

steps = 0

while n0 != 1:
    if n0 % 2 == 0:
        n0 = n0 // 2
    else:
        n0 = 3 * n0 + 1

    print(n0)
    steps += 1

print("steps =", steps)


# ==========================================
# 1b. WHILE LOOP - INFINITE LOOP
# ==========================================

# Example of an infinite loop:
# number = 1
# while number > 0:
#     print(number)

# Fixed version:

number = 5

while number > 0:
    print(number)
    number -= 1

print("The infinite loop was fixed.")


# ==========================================
# 1c. WHILE LOOP - CALCULATOR
# ==========================================

while True:
    first_number = int(input("Enter the first integer: "))
    second_number = int(input("Enter the second integer: "))

    print("Choose an arithmetic operation:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")

    operation = input("Enter your choice: ")

    if operation == "+":
        result = first_number + second_number
        print("Result =", result)

    elif operation == "-":
        result = first_number - second_number
        print("Result =", result)

    elif operation == "*":
        result = first_number * second_number
        print("Result =", result)

    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
            print("Result =", result)
        else:
            print("Cannot divide by zero.")

    else:
        print("Invalid operation.")

    choice = input("Do you want to continue? ")

    if choice != "Y" and choice != "y":
        print("Have a good day.")
        break


# ==========================================
# 2a. FOR LOOP - COUNT CHARACTERS
# ==========================================

text = input("Enter a sentence: ")

counts = {}
total_alphabets = 0

for character in text:

    # Count only English letters A-Z
    if not ("a" <= character.lower() <= "z"):
        continue

    character = character.lower()

    total_alphabets += 1

    if character in counts:
        counts[character] += 1
    else:
        counts[character] = 1

print("Total number of alphabets:", total_alphabets)
print("Total number of distinct alphabets are:")

for character in counts:
    print(character, "=", counts[character])


# ==========================================
# CHALLENGES
# ==========================================

print("\nChallenges")

print("One challenge I faced during this exercise was understanding how while loops work and how to stop an infinite loop. I also had to make sure the calculator worked with different operations. Another challenge was counting each letter while ignoring spaces, punctuation, and numbers. This exercise helped me understand how loops and conditions work together.")
