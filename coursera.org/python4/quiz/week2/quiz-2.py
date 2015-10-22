def add_up(n):
    if n == 0:
        return 0
    else:
        return n + add_up(n - 1)

print add_up(10)
