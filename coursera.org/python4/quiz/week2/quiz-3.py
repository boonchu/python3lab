def multiply_up(n):
    if n == 0:
        return 1
    else:
        return n * multiply_up(n - 1)

print multiply_up(10)
