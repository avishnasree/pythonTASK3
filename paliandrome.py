# check the given number is palindrome or not

def is_palindrome(number):
    num_str = str(number)# num to str
    reversed_str = num_str[::-1]# revers the str

    if num_str == reversed_str:
        return True
    else:
        return False


num = 123
if is_palindrome(num):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")