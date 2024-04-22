#Python program to create a Pyramid of numbers from 1 to 20 using For loop

def print_number_pyramid():
    n = 1  # Starting number
    max_number = 20  # End number in the pyramid

    for i in range(1, 7):  # Number of rows
        print(" " * (6 - i), end="")  # Print leading spaces for alignment
        for j in range(i):
            if n > max_number:  # Check if we have reached the maximum number
                break
            print("{:2d}".format(n), end=" ")  # Print number with 2-digit width
            n += 1  # Increment number for the next iteration
        print()  # Move to the next line for the next row
print_number_pyramid() # Call the function to print the number pyramid