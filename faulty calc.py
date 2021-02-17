while(1):
    print("Plz select the operation to be performed: +, -, *, /. \n Type 'break' to exit.")
    op=input()
    if (op== "+" or op== "-" or op== "*" or op== "/" or op=="break"):
        print("Enter 1st no.")
        n1=int(input())
        print("Enter 2nd no.")
        n2=int(input())

        if op== "+":
            if n1==1 and n2==1:
                print("\n Sum is equal to = 333")
            else:
                print ("\n Sum is equal to =", n1+n2)

        elif op== "-":
            if n1==2 and n2==2:
                print("\n Difference is equal to = 999")
            else:
                print ("\n Difference is equal to = ", n1-n2)        

        elif op== "*":
            if n1==2 and n2==2:
                print("\n Multiplication is equal to = 0")
            else:
                print ("\n Multiplication is equal to = ", n1*n2)
    
        elif op== "/":
            if n1==10 and n2==10:
                print("\n Division is equal to = 50")
            else:
                print ("\n Division is equal to = ", n1/n2)

        elif op=="break":
            exit()
    
    else:
        print("Enter valid input :<")
        