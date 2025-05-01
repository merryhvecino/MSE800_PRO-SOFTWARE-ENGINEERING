def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= 1
    return result

def check_prime(num):
    if num > 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

def display(num):
    print(f"Factorial of", num, "is", factorial(num))
    if check_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
        
display(10)
        