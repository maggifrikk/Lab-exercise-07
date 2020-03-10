def FizzBuss(num):
    if num % 5 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0 and num % 3 != 0:
        return "Buzz"