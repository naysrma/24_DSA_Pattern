#Regex (Regular Expression): A pattern used to search, match, extract, or replace specific text in a string.
#re.sub(): A Python function that replaces text matching a regex pattern with something else.


import re


def isPalindrome(s: str) -> bool:
    # Use regex to remove all non-alphanumeric characters and convert to lowercase
    newString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Initialize two pointers
    left, right = 0, len(newString) - 1
    
    # Check for palindrome by comparing characters from both ends
    while left < right:
        if newString[left] != newString[right]:
            return False
        left += 1
        right -= 1
    
    return True
arr = "A man, a plan, a canal: Panama"
print(isPalindrome(arr))
