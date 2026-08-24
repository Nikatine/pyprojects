'''
#List
def fibonacci_with_list(n):
    fib_series = [0, 1]
    for i in range (2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

n = 15
result = fibonacci_with_list(n)
print("Fibonacci series with ", n, "elements: ", result)
'''

#Variables
def fibonacci_with_vars(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = 10
print(f"Fibonacci series with {n} values: ")
fibonacci_with_vars(n)