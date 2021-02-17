def fibo(n):
    i=0
    
    while i<=n:
        a = fibo(i-1)+fibo(i+2)
        i=+1
        print(i)
    return a

no=int(input("Enter a number: "))
print("Ans is ",fibo(no))
