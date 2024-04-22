#importamos librerias 
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

#ingreso de datos 
#fx = lambda x: np.sqrt(x)*np.sin(x)
#a = 1
#b = 3
#n = 32
print("Ingrese la expresión de la función f(x), por ejemplo: 3*x**2 + 6*x + 2")
expr = input("f(x) = ")
x = symbols('x')
fx = lambdify(x, expr, 'numpy')

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
n = int(input("Ingrese el valor de n: "))
#procedimiento
m = n + 1
h = (b - a)/n
suma = 0
xi = a

for i in range(0,n,1):
    Atrapecio = h*(fx(xi)+fx(xi+h))/2
    suma = suma + Atrapecio
    xi = xi + h
integral = suma

muestras = n +1
xi = np.linspace(a,b,muestras)
fi = fx(xi)

muestraslinea = muestras*10
xk = np.linspace(a,b,muestraslinea)
fx = fx(xk)

#salida
print ("tramos :",n)
print ("integral", integral)

plt.plot(xi,fi,"ro")
plt.plot(xk,fx)

#trapecios
plt.fill_between(xi,0,fi,color="g")
for i in range(0,muestras,1):
    plt.axvline(xi[i],color="w")
plt.show()

