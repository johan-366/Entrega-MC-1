

import matplotlib.pyplot as plt

ε = 0.00005         #temps que passa entre mesures, és un valor arbitràriament petit
exponent = 2.641    #exponent de la formula de la força
x = [0.598]         #llista on hi ha els valors de la x de moment només hi ha el valor de x en t=0
y = [0]             #llista on hi ha els valors de la y de moment només hi ha el valor de y en t=0
vx = [0]            #llista on hi ha els valors de la v en l'eix x de moment només hi ha el valor de vx en t=0
vy = [0.559]        #llista on hi ha els valors de la v en l'eix y de moment només hi ha el valor de vy en t=0


#fem una iteració amb el número de vegades que ens interessa per a que fagi 4 oscil·lacions i apliquem el mètode de Euler per x, y ,vx i vy
for i in range (680000):
    x.append(x[i]+vx[i]*ε)
    y.append(y[i]+vy[i]*ε)
    vx.append(vx[i]-x[i]*(x[i]**2+y[i]**2)**((exponent-1)/2)*ε)
    vy.append(vy[i]-y[i]*(x[i]**2+y[i]**2)**((exponent-1)/2)*ε)

#representem el gràfic de la trajectòria de l'òrbita durant les 4 primeres voltes
plt.figure(figsize=(5,5))
plt.plot(x, y)
plt.show()