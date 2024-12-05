

import numpy as np
import matplotlib.pyplot as plt

r_pericentre = 0.598   #Radi al pericentre
v_pericentre = 0.559   #Velocitat al pericentre
exponent = 2.641       #Exponent que té la fòrmula de la força
m = 1                  #Massa de la partícula

L = m*r_pericentre*r_pericentre*v_pericentre/r_pericentre   #moment angular de la partícula
l = L/m

u0 = 1/((m*l**2)**(1/(3+exponent)))   #u de l'orbita si fos circular
h0 = (1/r_pericentre)-u0              #h de l'orbita en el pericente
A = h0

#d^2u/(dΘ)^2 i les seves respectives derivades respecte u, totes elles per u=u0
Ψ_0 = u0
Ψ1_0 = -(exponent+2)
Ψ2_0 = (exponent+2)*(exponent+3)*u0**(-1)
Ψ3_0 = -(exponent+2)*(exponent+3)*(exponent+4)*u0**(-2)

#Valor de les β^2 per cada ordre i valor de β^2 total, que és la suma de les anteriors
α2 = 1-Ψ1_0
β2_1 = 0
β2_2 = -((5*(Ψ2_0**2)+3*α2*Ψ3_0)*A**2)/(24*α2)
β2 = α2+β2_1+β2_2

#Utilitzant les fòrmules que hem vist anteriorment
def r(Θ):
    h_0 = A*np.cos(β2**(1/2)*Θ)
    h_1 = (Ψ2_0*A**2*(3-np.cos(2*(β2**(1/2)*Θ))-2*np.cos(β2**(1/2)*Θ)))/(12*α2)
    h_2 = (29*(Ψ2_0/α2)**2+3*Ψ3_0/α2)*A**3*np.cos(β2**(1/2)*Θ)/576+(Ψ2_0/α2)**2*A**3*np.cos(2*β2**(1/2)*Θ)/36+((Ψ2_0/α2)**2-Ψ3_0/α2)*A**3*np.cos(3*β2**(1/2)*Θ)/192
    h = h_0+h_1+h_2
    return 1/(u0+h)

#Fem que Θ tingui valors de entre 0 i 8pi amb diferència de 8pi/10000 entre dos consecutius
Θ = np.linspace(0, 8 * np.pi, 10000)

#Passem les cordenades a polars
x = r(Θ)*np.cos(Θ)
y = r(Θ)*np.sin(Θ)


plt.figure(figsize=(5,5))
plt.plot(x, y)
plt.show()

