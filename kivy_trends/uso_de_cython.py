import os
os.system('cls')

# def f(x):
#     return x**2-x

def integrate_f(a,b,N):
    cdef int i=0
    cdef double s,dx
    s=0
    dx=(b-a)/N
    for i in range(N):
        s+=f(a+i*dx)
    
    return s*dx

# cdef double f(double x):
#     return x**3-x

# a=f(4)
b=integrate_f(2,3,5)

print(a)
print(b)

