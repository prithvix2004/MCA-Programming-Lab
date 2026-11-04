#8. Regular Expressions
#8 (a) Write a Python program that matches a word at the beginning of a string.
def match_start_word(text, word):
    # Checks if the string begins with the specified word
    if text.startswith(word):
        return f"Match found! The string starts with '{word}'."
    else:
        return f"No match. The string does not start with '{word}'."

#Example
sentence = "Python is an excellent programming language."

print(match_start_word(sentence, "Python"))
print(match_start_word(sentence, "excellent"))

#8 (b) Write a Python function to find and return all numbers/digits present in a given sentence.
def find_individual_digits(sentence):
    # Iterates through every character and keeps it if it is a digit
    return [char for char in sentence if char.isdigit()]

# Example:
text = "Room 404 was booked 2 times."
print(find_individual_digits(text))

#8 (c) Write a Python program to check if a string matches a pattern that has an a followed by zero or more b’s.
def matches_pattern(text: str) -> bool:
    # An 'a' followed by zero or more 'b's means the string must start with 'a'
    if not text.startswith('a'):
        return False
        
    # After removing the mandatory 'a', the rest of the string must only contain 'b's
    remaining_text = text[1:]
    
    # If remaining_text is empty, it means the string was just "a" (0 'b's), which is valid.
    # If it is not empty, all characters must be 'b'.
    return all(char == 'b' for char in remaining_text)

#Example:
test_strings = ["a", "ab", "abb", "abbb", "b", "abc", "ba", "aab", ""]

print(f"{'String':<10} | {'Matches':<8}")
print("-" * 23)
for text in test_strings:
    print(f"{repr(text):<10} | {matches_pattern(text)}")
