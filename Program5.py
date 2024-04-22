#Python program that takes a string and returns true if it is a palindrome, false otherwise

def is_palindrome (input_string):
    input_string = input_string.replace(" ","").lower() # Remove spaces and convert to lowercase for case-insensitive comparison
    return input_string == input_string[::-1] # Compare the string with its reverse

input_string = "No lemon, no melon"
print("Is it a palindrome?", is_palindrome(input_string))
    