
# Initialize a variable to store the total sum
total = 0

# Use a while loop to continuously ask for numbers
while True:
    # Ask the user for input and convert it to an integer
    user_input = input("Enter a number (or a negative number to quit): ")
    number = int(user_input)

    # Check if the number is negative
    if number < 0:
        break  # Exit the loop if the number is negative

    # Add the positive number to the total
    total += number

# Print the total sum of positive numbers
print("The sum of positive numbers entered is:", total)
