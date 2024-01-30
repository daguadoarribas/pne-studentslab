x = 0
y = 1
print(x)
for i in range(10):
    z = y
    y = x + y
    x = z
    print(x)