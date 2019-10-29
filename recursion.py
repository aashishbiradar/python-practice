import time 
def factorial_loop(n):
    fact = 1
    while n > 1:
        fact = fact * n
        n -= 1
    return fact

def factorial_recursion(n):
    return 1 if n == 1 else (n * factorial_recursion(n-1))

t1 = time.time()
#factorial_loop(1000)
factorial_recursion(1000)
t2 = time.time()
print(t2-t1)