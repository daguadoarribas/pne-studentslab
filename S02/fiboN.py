def fibon(n):
    x = 0
    y = 1
    for i in range(n - 1):
        z = y
        y = x + y
        x = z
    return x

term_5 = fibon(5)
print(f"The 5th term is: {term_5}")
term_10 = fibon(10)
print(f"The 10th term is: {term_10}")
term_15 = fibon(15)
print(f"The 15th term is: {term_15}")




