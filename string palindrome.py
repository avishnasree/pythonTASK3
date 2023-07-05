#check if a string is a palindrome.
def is_palindrome(string):
    string = string.replace("","").lower()
    reversed_str = string[::-1]


    if string == reversed_str:
        return True
    else:
        return False


word = "radar"
if is_palindrome(word):
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")