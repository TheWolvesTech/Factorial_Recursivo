# Recursive Factorial with function.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


#Entry Point.
if __name__ == '__main__':
    q = int(input("Enter a quantity : "))
    i = 0
    while i < q:
        number = int(input("Enter a number : "))
        print(f"the factorial of {number} is :", factorial(number))
        i += 1
