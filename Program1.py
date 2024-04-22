#Python program to calculate total number of vowels and count of each individual vowel A, E, I, O, U in the string "Guvi Geeks Network Private Limited"

# Define the input string
input_string = "Guvi Geeks Network Private Limited"

# Convert the string to lowercase to make the counting case-insensitive
input_string = input_string.lower()

# Initialize counters for total vowels and individual vowels
total_vowels = 0
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Iterate through each character in the string
for char in input_string:
    # Check if the character is a vowel
    if char in 'aeiou':
        # Increment total vowels count
        total_vowels += 1
        # Increment count of individual vowels
        vowel_counts[char] += 1

# Print the total count of vowels and count of each individual vowel
print("Total vowels:", total_vowels)
for vowel, count in vowel_counts.items():
    print(vowel, ":", count)