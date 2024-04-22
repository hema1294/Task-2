#Python program that takes a string and retuns the numbers of words in it

def count_words(input_string):
    # Split the string into words based on whitespaces
    words = input_string.split()
    
    # Return the number of words which gives the count of the words
    return len(words)

input_string = "A Hello World program is a simple program"
word_count = count_words(input_string)
print("Number of Words:", word_count)