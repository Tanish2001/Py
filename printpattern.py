n=int(input("Enter a no.:"))
i=0
if n%2==0:
    print("Even")
    for i in range(0,n+1):
        print("*"*i)

elif n%2==1:
    print("Odd")
    for i in range(n,0,-1):
        print("*"*i)
        