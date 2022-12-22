from traceback import print_tb
import math

def Fibonaci(a,b,err):
    n=1
    while(abs(b-a)/err)>fibbr(n):
        n+=1

    x1=a+fibbr(n-2)/fibbr(n)*(b-a)
    x2=a+b-x1

    for i in range(2, n+1):

        if func(x1)<=func(x2):
            b=x2
            x2=x1
            x1=a+b-x2
        else:
            a=x1
            x1=x2
            x2=a+b-x1

    if(func(x1)<func(x2)):
        xopt=x1
        fopt=func(x1)
    else:
        xopt=x2
        fopt=func(x2)

    return xopt, fopt, n

def func(x):
    f = 2*x**4 - 3*x
    return f

def fibbr(n):
    if n<=1:
        return n
    else:
        return (fibbr(n-1)+fibbr(n-2))

a=0
b=1
err=0.00001
xopt,fopt,n=Fibonaci(a,b,err)

#print(xopt, fopt, n)



def Zlatni_presek(a,b,err):
    c=(3 - math.sqrt(5))/2
    x1=a+c*(b-a)
    x2=a+b-x1
    n=1
    
    while (b-a)>err:
        n+=1
        if func(x1)<=func(x2):
            b=x2
            x1=a+c*(b-a)
            x2=a+b-x1
        else:
            a=x1
            x1=a+c*(b-a)
            x2=a+b-x1

    if func(x1)<func(x2):
        xopt=x1
        fopt=func(x1)
    else:
        xopt=x2
        fopt=func(x2)

    return xopt, fopt, n

xopt,fopt,n=Zlatni_presek(a,b,err)

print(xopt, fopt, n)