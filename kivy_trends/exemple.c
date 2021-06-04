from libc.math import sin

cdef double f(double x) except *:
    return sin(x**2)