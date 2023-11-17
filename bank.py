# write the program to bank transaction

def add(x,y):
    z=x+y
    return z
def sub(x,y):
    return x-y
def mul (x,y):
    return x*y
def div (x,y):
    return x/y
def exp(x,y):
    return x**y
def fd(x,y):
    return x//y

while True:

    print("ARITHMETIC OPERTOR OR CALCULATORS")
    print("..................................")
    print("1.ADDTION")
    print("2.SUBSTRACTION")
    print('3.MULTIPUCTION')
    print('4.DIVISION')
    print("5.exponetial")
    print("6.floor division")
    print("7.exit")
    a=int(input("enter the first numeber"))
    b=int(input("enter the second number"))
    ch=int(input("which type arithmetic opetor you want"))
    if ch==1:
        c=add(a,b)
        print(c)

    elif ch==2:
        c=add(a,b)
        print(c)

    elif ch==3:
        c=mul(a,b)
        print(c)
    elif ch==4:
        c=div(a,b)
        print(c)
    elif ch==5:
        c=exp(a,b)
        print(c)
    elif ch==6:
        c=fd(a,b)
        print(c)
    elif ch==7:
        break
    
    else:
        print("invilid fund plzz try again ")

        
