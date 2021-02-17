#f=open("E:\\Python Programs\\hello.txt","a")
#a=f.write("Hello World!!\n")
#print(a)
#f.close()
with open ("E:\\Python Programs\\hello.txt") as f:
    a=f.readlines()
    print(a)
f=open("E:\\Python Programs\\hello.txt","r+")
print(f.read())
a=f.write("Bye world!!!")
print(a)


