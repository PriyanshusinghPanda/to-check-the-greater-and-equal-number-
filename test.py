a = int(input("enter a :- "))
b = int(input("enter b :- "))
c = int(input("enter c :- "))
if a>=b and a>=c:
    if a>b and a>c and a!=b and a!=c and b!=c:
        print("a is greater")
    if a>b and a>c and a!=b and a!=c and b==c:
        print("a is greater and b and c are equal")
    if a==b==c:
        print("all are equal")
    if a==b and a!=c :
        print("a is greater than c and equal to b")
    if a==c and a!=b:
        print("a is greater than b and equal to c")
if b>=a and b>=c:
    if b>a and b>c and b!=a and b!=c and a!=c:
        print("b is greater")
    if a>b and a>c and a!=b and a!=c and a==c:
        print("b is greater and a and c are equal")
    if b==c and b!=a:
        print("b is greater than a and equal to c")
if c>=b and c>=a:
    if a>b and a>c and a!=b and a!=c and a!=b:
        print("c is greater")
    if c>b and c>a and c!=b and c!=b and a==b:
        print("c is greater and a and b are equal")
