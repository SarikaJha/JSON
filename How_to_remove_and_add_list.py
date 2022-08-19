list=int(input("enter the length of list:"))
i=0
a=[]
x=[]
while i<list:
    b=input("enter the items:")
    c=input("enter 'add' to add and 'remove' to remove item:")
    if c=="add":
        a.append(b)
    elif c=="remove":
        a.remove(b)
    else:
        print("invalid input")
    i+=1
print(a)
