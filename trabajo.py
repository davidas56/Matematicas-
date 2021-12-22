#hecho por jose david rojas diaz cod 1090511968

import math
def suma(x,y):
    z= x+y
    return z
def resta(x,y):
    z = x-y
    return z
def multiplicacion(x,y):
    z = x*y
    return z
def division(x,y):
    z = x/y
    return z
def residuo(x,y):
    z = divmod(x,y)
    return z
def numero_primo(x):
         for i in range (2,x):
        if x%i==0:
            return "is not prime"
        return "is prime"
def raiz_cuadrada(x,y):
    x = math.sqrt(x)
    y = math.sqrt(y)
    return z
def area_del_triangulo(x,y):
    z = x*y/2
    return z 
def calculo_pendiente(x,y,a,b):
    z = (x-y)/(a-b)
    return z
a =5
b=7
c=8
z=9
a = suma(a,b)
print("la suma fue", a)
b = resta(a,b)
print("la resta fue", b)
c = multiplicacion(a,b)
print("la multiplicacion fue", c)
d = division(a,b)
print("la division fue ", d)
e = residuo(a,b)
print("el residuo fue ", e)
f = raiz_cuadrada(a,b)
print("la raiz cuadrada resultante fue ", f)
print(prime(c))
g = area_del_triangulo(a,b)
print("el area del triangulo resultante fue ", g)
y = calculo_pendiente(a,b)
print("el calculo de pendiente fue  resultante fue ", y)