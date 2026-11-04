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
