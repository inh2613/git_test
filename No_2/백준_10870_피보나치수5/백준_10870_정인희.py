def p(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n = p(n - 1) + p(n - 2)
        return n


n = int(input())

print(p(n))


