#Python program that takes a string and returns the number of uniques characters in it
def count_unique_characters(input_string): 
    unique_characters = set(input_string)  #Create a set to store the count of unique characters
    return len(unique_characters) # Return the number of unique characters
input_string = "A Hello World is generally a simple program"
unique_characters = count_unique_characters(input_string)
print ("Number of unique characters:", unique_characters)