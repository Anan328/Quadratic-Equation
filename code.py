while True:
    import math
    try:
        a=int(input("enter the value of 'a':"))
        if a==0:
            print("the value of 'a' can't be zero")
        else:
            b=int(input("enter the value of 'b':"))
            c=int(input("enter the value of 'c':"))
            if a==1:
                print("The required Quadratic Eqn is:"," ",end="")
                print("x"+"^"+"2","+","("+str(b)+")" + "x","+","("+str(c)+")","=","0")
            else:
                print("The required Quadratic Eqn is:"," ",end="")
                print(str(a) + "x"+"^"+"2","+","("+str(b)+")" + "x","+","("+str(c)+")","=","0")
            d=(b**2)-(4*a*c)
            if d>=0:
                x1=(-b+math.sqrt(d))/(2*a)
                x2 = (-b - math.sqrt(d)) /(2 * a)
                print("The real roots are:",round(x1,3),"and",round(x2,3))
            else:
                d1=((math.sqrt(math.copysign(d,0))) / (2 * a))
                z=(-b)/(2*a)
                print("The complex roots are:",str(round(z,3))+"+"+str(round(d1,3))+"i","and",str(round(z,3))+"-"+str(round(d1,3))+"i")
    except Exception as e:
        print("following error encountered:",e)
