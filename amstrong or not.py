# check the given number is armstrong or not

def is_armstrong(number):
    num_str = str(number)#convert num to str
    num_digits = len(num_str)

    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)#calculate the sum of the cubes of each digits

    if armstrong_sum == number:#check if the sum is equal to the number
        return True
    else:
        return False
num = 15
if is_armstrong(num):
    print(num,"is an armstrong number")
else:
    print(num,"is not a armstrong number")