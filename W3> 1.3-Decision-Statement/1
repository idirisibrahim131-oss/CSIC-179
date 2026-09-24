# 1. Comparison Operators

print(2 < 5)
print(10 <= 10)

x = 10
print(20 < x)

print("A" < "a")
print("Monday" > "Tuesday")


# ASCII Characters

for number in range(32, 127):
    print(chr(number), "=", number)


# 2. Logical Operators

print(10 > 4 and 50 < 100)
print(10 < 4 and 50 < 100)

print(10 < 4 or 50 > 100)
print(10 > 4 or 50 > 100)

print(not (10 > 4))
print(not (10 < 4))


# 3. Bitwise Logical Operators

x = 0b1110
y = 0b1011

result = x | y

print(result)
print(bin(result))

print(x & y)
print(~x)
print(x ^ y)


# 4. Largest of Two Integers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("The larger number is:", larger_number)


# Nested Conditional Statements

x = 10

if x > 5:
    if x == 6:
        print("nested: x == 6")
    elif x == 10:
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")


# 5a. Largest Three Integers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3

print("The largest number is:", largest)


# 5b. Even or Odd

number = int(input("Enter an integer: "))


# Approach 1

if number % 2 == 0:
    print("Approach 1: even")
else:
    print("Approach 1: odd")


# Approach 2

if number / 2 == number // 2:
    print("Approach 2: even")
else:
    print("Approach 2: odd")


# Approach 3

if number & 1:
    print("Approach 3: odd")
else:
    print("Approach 3: even")


# 5c. CISC 179 Grading Scheme

percentage = int(input("Enter your percentage: "))

if percentage > 90:
    print("Grade: A")
    print("Description: Work of genuinely superior quality.")
elif percentage >= 80:
    print("Grade: B")
    print("Description: Passing performance falls approximately in the upper distribution of passing grades.")
elif percentage >= 71:
    print("Grade: C")
    print("Description: Passing performance falls approximately in the center of the distribution of all passing grades.")
elif percentage >= 65:
    print("Grade: D")
    print("Description: Passing performance falls approximately in the lower distribution of passing grades.")
else:
    print("Grade: F")
    print("Description: Failing performance that does not satisfy the basic requirements of the course and needs to be improved in significant ways.")


# 5d. Bitwise AND

number = int(input("Enter an integer: "))

if number & 1:
    print("The number is odd.")
else:
    print("The number is even.")


# 6. Code Revision

name = input("What's your name? ")
current_time = int(input("What time is it? "))

if current_time < 1200:
    print("Hi " + name + ", good morning!")
elif current_time < 1800:
    print("Hi " + name + ", good afternoon!")
else:
    print("Hi " + name + ", good evening!")

print("Good Bye")


# 7. Output Verification

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")

if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")


# Truth Table - AND

print("AND Truth Table")
print("A     B     A and B")

print(False, False, False and False)
print(False, True, False and True)
print(True, False, True and False)
print(True, True, True and True)


# Truth Table - OR

print("OR Truth Table")
print("A     B     A or B")

print(False, False, False or False)
print(False, True, False or True)
print(True, False, True or False)
print(True, True, True or True)


# Truth Table - NOT

print("NOT Truth Table")
print("A     not A")

print(False, not False)
print(True, not True)


# Truth Table - XOR

print("XOR Truth Table")
print("A     B     A ^ B")

print(False, False, False ^ False)
print(False, True, False ^ True)
print(True, False, True ^ False)
print(True, True, True ^ True)
