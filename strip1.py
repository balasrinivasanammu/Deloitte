txt = "---chennai----bbcckk????"

x = txt.rstrip("-bk?")

print(x)




'''









The strip() method in Python is used to remove leading and trailing
whitespace characters (such as spaces, tabs, and newline characters)
from a string. It can also be used to remove specific characters
from the start and end of a string if you specify them


# Example 2: Using strip() to remove specific characters
text = "xxchennai, cityxx"
cleaned_text = text.strip('x')

print(f"Original text: '{text}'")
print(f"After strip('x'): '{cleaned_text}'")



# Example 3: Removing unwanted spaces from user input
user_input = input("Please enter your name with extra spaces: ")

# Removing leading and trailing spaces
cleaned_input = user_input.strip()

print(f"Original input: '{user_input}'")
print(f"Cleaned input: '{cleaned_input}'")

'''

