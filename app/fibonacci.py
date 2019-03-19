def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
        if a < num:
            yield a
        else:
            break

def count_fib(first, second):
    lst = []
    for fib in fibonacci(int(second)):
        if fib >= int(first):
            lst.append(fib)
        else:
            continue
    return print(lst)