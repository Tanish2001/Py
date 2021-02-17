l1=["a",10,0,20,5,2,"g",50,100,999,55,100]
#print(l1)
for item in l1:
    if str(item).isnumeric() and item>6:
        print(item)
    