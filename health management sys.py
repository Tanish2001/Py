print("Welcome to Health Manage System")
client=input("Plz enter Client Name.\n")
if client=="Tan":
    f=open("E:\\Python Programs\\Tan.txt", "r+")
elif client=="Man":
    f=open("E:\\Python Programs\\Man.txt", "r+")
elif client=="Kan":
    f=open("E:\\Python Programs\\Kan.txt", "r+")
a=f.readline()
print(a)
def getdate():
    import datetime
    return datetime.datetime.now()
details=input("Enter the details u want to add\n")
a=f.write(  details "\n")


