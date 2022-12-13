def area1(x):
    l=int(input("enter length"))
    b=int(input("enter bradth"))
    r=l*b
    return r
def area2(x):
    s=int(input("enter side of square"))
    r= s * s
    return r
def add(a):
    b=int(input("enter first number"))
    c=int(input("enter second nunmber"))
    r=b+c
    return r
def sub(a):
    b=int(input("enter first number"))
    c=int(input("enter second nunmber"))
    r=b-c
def mul(a):
    b=int(input("enter first number"))
    c=int(input("enter second nunmber"))
    r=b*c
    return r
def div(a):
    b=int(input("enter first number"))
    c=int(input("enter second nunmber"))
    r=b/c
    return r
def pow(a):
    b=int(input("enter first number"))
    c=int(input("enter second nunmber"))
    r=b**c
    return r
def mod(a):
    b=int(input("enter first number"))
    c=int(input("enter second nunmber"))
    r=b%c
    return r
while True:
    a=int(input("enter 1 for area of rectangle 2 for area of square 3 for sum of two numbers 4 for difference of two numbers 5 for product of two numbers 6 for quotient of two numbers 7 for exponent of two numbers  8 for remainder of two numbers"))
    if a==1:
        print("area of rectangle is",area1(a))
    elif a==2:
        print("area of square is",area2(a))
    elif a==3:
        print("sum of two numbers",add(a))
    elif a==4:
        print("difference of two numbers",sub(a))
    elif a==5:
        print("product of two numbers",mul(a))
    elif a==6:
        print("quotient of two numbers", div(a))
    elif a==7:
        print("exponent of two numbers",pow(a))
    elif a==8:
        print("remainder of two numbers",mod(a))
    else:
        print("invalid input")
    k=input("enter yes to repeat and no for finish")
    if k=="yes":
        continue
    elif k=="no":
        break
    else:
        print("invalid input")