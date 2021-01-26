import math


def sum_complex(a, b): return a[0] + b[0], a[1] + b[1]


def res_complex(a, b): return a[0] - b[0], a[1] - b[1]


def mult_complex(a, b): return a[0]*b[0] - a[1]*b[1], a[1]*b[0] + a[0]*b[1]


def div_complex(a,b):
    a1 = a[0]*a[1] + b[0]*b[1]
    b1 = a[1]*b[0] - a[0]*b[1]
    c = a[1]**2 + b[1] ** 2
    return a1/c , b1/c


def modulo_complex(a): return((a[0])**2 + (a[1])**2)**(1/2)


def conjugado_complex(a): return a[0],-a[1]


def convercar_complex(a): return modulo_complex(a), math.tan(a[1]/a[0])


def converpo_complex(a): return a[0] * round(math.cos(a[1]),1), a[0] * round(math.sin(a[1]), 1)


def fase_complex(a): return round(math.degrees(math.atan(a[1]/a[0])))