def add(a,b):
    print(a+b)
def cikar(a,b):
    print(a-b)
def carp(a,b):
    print(a*b)
def bol(a,b):
    print(a/b)
n = True
while n:
    a=input("enter number 1:")
    b=input("enter number 2:")
    a= float(a)
    b=float(b)
    c = input("which operations: ")
    if c == "+":
        add(a,b)
    elif c=="-":
        cikar(a,b)
    elif c == "*":
        carp(a,b)
    elif c == "/":
        bol(a,b)
    else:
        print("gecerli isaret giriniz")
    d = input("devam mi tamam mi 'y'? 'n'")
    if d == "n":
        n = False

