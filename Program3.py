#Python program that takes a string and returns a new string with all the vowels removed

# Define the input string
input_string = "Guvi Geeks Network Private Limited"

def remove_vowels(input_string): #Define a string containig all vowels both uppercase and lowercase
    vowels = "aeiouAEIOU"
    result_string = "".join(char for char in input_string if char not in vowels)
    return result_string
result = remove_vowels(input_string)
print("Original String:", input_string)
print("String with vowels removed:", result)