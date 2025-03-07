
def fibonacci_sequence(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


for i in range(10):
    print(fibonacci_sequence(i))
