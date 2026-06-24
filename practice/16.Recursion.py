def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))



def countdown(n):
    if n == 0:
        print("Done")
        return

    print(n)
    countdown(n - 1)

countdown(5)