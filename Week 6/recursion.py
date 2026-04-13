def fact (n):
    if (n==0):
        return 1
    if (n==1):
        return 1
    elif(n>1):
        return(n*fact(n-1))
    else:
        print("incorrect n")

n=int(input('Enter a non negitive number : '))
if(n<0):
    print('Fact is not defined for negative number')
else:
    f=fact(n)
    print('Factorial of ',n,'is ', f)