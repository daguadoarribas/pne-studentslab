def fibon(n):
    x = 0
    y = 1
    fib_sequence = [x]

    for i in range(n - 1):
        z = y
        y = x + y
        x = z
        fib_sequence.append(x)

    return fib_sequence
def fibosum(n):
    fib_sequence = fibon(n)
    return sum(fib_sequence)

sum_5 = fibosum(5)
sum_10 = fibosum(10)

print(f"Sum of the first 5 Fibonacci terms is: {sum_5}")
print(f"The sum of the first 10 Fibonacci terms is: {sum_10}")