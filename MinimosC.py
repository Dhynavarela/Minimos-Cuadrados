#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
name = 'millikan' #Nombre del archivo
archivo = open(str(name) + '.txt', 'r') 
datos= archivo.readlines()
#print(datos)

X = []
Y = []

for i in range(len(datos)):
    datos[i] = datos[i].split()
    X.append(float(datos[i][0]))
    Y.append(float(datos[i][1]))
#print("Datos para X:",X)
#print("Datos para Y:",Y)
N = len(X)
print("EL número de datos es N=",N)

#a) Calculamos Ex, Ey, Exx, Exy
s = 0.0
for i in range(N):
    s = s + X[i]
Ex = s/N
print("Ex=",Ex)

s1 = 0.0
for i in range(N):
    s1 = s1 + Y[i]
Ey = s1/N
print("Ey=",Ey)

s2 = 0.0
for i in range(N):
    s2 = s2 + X[i]**2
Exx = s2/N
print("Exx=",Exx)

s3 = 0.0
for i in range(N):
    s3 = s3 + X[i]*Y[i]
Exy = s3/N
print("Exy=",Exy)

#Definimos m y c

m = (Exy-Ex*Ey)/(Exx-((Ex)**2))
print("m=",m)

c = (Exx*Ey-Ex*Exy)/(Exx-((Ex)**2))
print("c=",c)

#b) Recta con m y c obtenidas

x = np.arange(X[0]-1e14,X[N-1]+1e14,1e14) 
y = m*x+c

plt.figure()
plt.title('Ajuste lineal por mínimos cuadrados')
plt.plot(X,Y,'ro',x,y) #Ajuste con minimos cuadrados hechos paso a paso
plt.legend(('Datos experimentales','Ajuste lineal'), loc="upper left")
plt.title('Ajuste lineal por mínimos cuadrados')
plt.grid(color='B', linestyle='-', linewidth=0.1)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

#c) Obtener a los puntos y1 y y2 dados por m,c y x1, x2
x1 = 10e+14
x2 = 7.5e+14
y1 = m*x1+c
y2 = m*x2+c
print("y1=",y1, "que corresponde a ",x1)
print( "y2=",y2,"que correponde a",x2)

#d)Ajuste utilizando curve_fit
def f(m,c,x):
    return m*x + c

B,A = curve_fit(f, X, Y)[0]
x0 = np.arange(X[0]-1e14,X[N-1]+1e14,1e14) 
y0 = A*x0+B

plt.figure()
plt.title('Ajuste lineal por mínimos cuadrados con scipy')
plt.plot(X,Y,'ro',x0,y0) #Ajuste de recta con curve fit de scipy
plt.legend(('Datos experimentales','Ajuste lineal'), loc="upper left")
plt.grid(color='B', linestyle='-', linewidth=0.1)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()



#e) Constante de planck

#como Y = mX +c y por otro lado V=h/e*v-phi, analizando ambas ecuaciones y sabiendo que X=v e Y=V, se puede hacer
#m=h/e y -phi=c 

e = 1.602e-19 #Coloumbs
h = m*e 
print("El valor de la constante de planck es h=",h, "J.s")

