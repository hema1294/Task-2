#Python program that takes a string and returns the most frequent character in it

def most_frequent_character(input_string):
    char_freq = {} # Create a dictionary to store character frequencies
    for char in input_string:   # Count frequencies of each character in the input string
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    most_frequent_char = max(char_freq, key=char_freq.get) # Find the character with the highest frequency
    max_frequency = char_freq[most_frequent_char]
    return most_frequent_char, max_frequency
input_string = "Hello world program"
most_frequent, frequency = most_frequent_character(input_string)
print("Most Frequent Character:", most_frequent)
print("Frequency:", frequency)