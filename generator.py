from random import *
from string import *

length = int(input("Enter the length of the password: "))

print("You have selected the following length of the password:", length)

choice = int(input("Select your password type: "))
print("1. Alphanumeric", end=" ")
print("2. Alphabetic", end=" ")
print("3. Numeric", end=" ")
print("4. Alphanumeric with special characters", end=" ")
print("5. Alphabetic with special characters", end=" ")
print("6. Numeric with special characters", end=" ")
print("7. Alphanumeric with special characters and spaces", end=" ")
print("8. Alphabetic with special characters and spaces", end=" ")
print("9. Numeric with special characters and spaces", end=" ")
print("10. All in one", end=" ")