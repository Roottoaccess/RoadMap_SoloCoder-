# Coding and checking if the string is a palindrom or not ?

# Function to build Palindrom String Ckecking......
def palindrom_string_check(s):
    reversing_string = s[::-1]
    if s == reversing_string:
        return f'{s} is a palindrom string.....'
    else:
        return f'{s} is not a palindrom string.....'
# Calling the function......
string = input("Enter a string: ")
print(palindrom_string_check(string))