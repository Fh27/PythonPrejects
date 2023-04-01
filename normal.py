
def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
def factorial_recursive(n):

    if n == 1:
        return 1
    elif n==0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
n= int(input('enter'))
print(factorial_iterative(n))
print(factorial_recursive(n))
