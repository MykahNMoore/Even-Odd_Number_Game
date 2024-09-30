number = int(input("Enter a number here: "))

'''Function that checks if number is divisible by 2'''
def check_num(num):
    if num % 2 == 0:
        print("Your number is even!")
    elif num % 2 == 1:
        print("Your number is odd!")

check_num(number)