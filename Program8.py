#Python program that takes a string and returns true if it is an anagram of another string, false otherwise

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the sorted versions of the strings are the same
    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
print ("Are '{}' and '{}' anagrams?". format(string1, string2), result)