try:
    num = int(input("Enter an integer: "))
    if num < 0:
        num = -num  
    num_digits = 0
    while num > 0:
        num //= 10
        num_digits += 1
    print("Number of digits in the number:", num_digits)
except ValueError:
    print("Invalid input. Please enter a valid integer.")