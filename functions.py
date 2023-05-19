def chandu(a,b,c):
    if a>b and a>c:
        print(f"a is biggest{a}")
        print("have a nice day")
    elif b>c:
        print(f"b is biggest{b}")
        print("have a nice day")
    else:
        print(f"c is biggest{c}")
        print("have a nice day")
x=int(input("enter first number: "))
y=int(input("enter a second number: "))
z=int(input("enter a third number: "))
chandu(x,y,z)
