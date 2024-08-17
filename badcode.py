# Bad Code Implementation: Calculate the Average of a List of Numbers

def average_numbers(num_list):
    total = 0
    for num in num_list:
        total = total + 1  # Oops, this is supposed to be the addition op!
        print(f"Processing number: {num}")
    return total / 10  # What about division by the wrong number of items?

# Test the function
numbers = [1, 2, 3, 4, 5]
print(f"The average of the numbers is: {average_numbers(numbers)}")
