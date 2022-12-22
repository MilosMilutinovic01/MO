import numpy as np
import math

def newtonRaphson(x0,tol):
    x_novo=x0;
    x_pre=math.inf
    iter=0
    while(abs(x_pre-x_novo)>tol):
        iter+=1
        x_pre=x_novo
        x_novo=x_pre-dfunc(x_pre)/ddfunc(x_pre)
    xopt=x_novo
    fopt=func(xopt)
    return xopt,fopt,iter

def func(x):
    f=x**4-5*x**3-2*x**2+24*x
    return f
def dfunc(x):
    f=4*x**3-15*x**2-4*x+24
    return f
def ddfunc(x):
    f=12*x**2-30*x-4
    return f

tol=0.0001
init_guess=1
[xopt,fopt,iter]=newtonRaphson(init_guess,tol)
print(xopt,fopt,iter)

def secica(x0,x1,tol):
    x_pre=x0
    x_ppre=math.inf
    x_novo=x1
    iter=0
    while(abs(x_novo-x_pre)>tol):
        iter+=1
        x_ppre = x_pre
        x_pre = x_novo
        x_novo=x_pre-dfunc(x_pre)*(x_pre-x_ppre)/(dfunc(x_pre)-dfunc(x_ppre))
    xopt=x_novo
    fopt=func(xopt)
    return xopt,fopt,iter

def func(x):
    f=x**4-5*x**3-2*x**2+24*x
    return f
def dfunc(x):
    f=4*x**3-15*x**2-4*x+24
    return f

tol=0.0001
init_guess1=0
init_guess2=3
[xopt,fopt,iter]=secica(init_guess1,init_guess2,tol)
print(xopt,fopt,iter)