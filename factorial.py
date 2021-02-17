
def fac_iterative0(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac



def fac_recursive(n):
    if no==1 or no==0:
        return 1
    else:
        return n * fac_recursive(n-1)

no=int(input("Enter the no.: "))
print("Factorial is using iteration is", fac_iterative0(no))
print("Factorial is", fac_recursive(no))









