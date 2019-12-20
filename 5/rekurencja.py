def factorial(n):
    if n < 0:
        return 
    s = i = 1
    while i <= n:
        s = s * i
        i=i+1
    return s

def fibonacci(n):
    if n == 1 | n ==2:
        return 1
    else:
        a = 1
        b = 1
        i=3
        while i <= n:
            temp = a + b
            a = b
            b = temp
            i = i+1
    return b