# # i = 1
# # while i < 5:
# #     print(i)
# #     i += 1
# # else:
# #     print("else:", i)

# # Store the current largest number here.
# largest_number = -999999999

# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))

# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))

# # Print the largest number.
# print("The largest number is:", largest_number)

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)



