#Python program that takes two strings and returns the longest common substring between them

def longest_common_substring(str1, str2):
    # Initialize variables to store the length of the longest common substring and its ending index
    max_length = 0
    end_index = 0
    
    # Initialize a 2D matrix to store the lengths of the longest common suffixes
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Iterate through each character of both strings
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # If characters match
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                # Update max_length and end_index if needed
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_index = i
            else:
                matrix[i][j] = 0
    
    # Extract the longest common substring using the ending index and max_length
    longest_substring = str1[end_index - max_length:end_index]
    
    return longest_substring

# Example usage
str1 = "abcdefg"
str2 = "xyzabcde"
print("Longest common substring:", longest_common_substring(str1, str2))