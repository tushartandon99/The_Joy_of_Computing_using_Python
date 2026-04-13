def fibonacci (n):
    if(n<2):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input('Enter a non negitive number :'))
if(n<0):
    print("Undefined for negative number")
else:
    fab=fibonacci(n)
    print('Fibonacci at ',n,'th position : ',fab)