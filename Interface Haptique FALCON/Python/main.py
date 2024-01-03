#!/usr/bin/env python3

from pyDhd import *
from functions import *
# from pylab import *
import numpy as np
from math import sin, cos

done = False

dhdOpen()

posx = list()
posy = list()
posz = list()

Forcex = list()
Forcey = list()
Forcez = list()

while not done:
    k = 2000
    c = 0

    ret, px, py, pz = dhdGetPosition()
    ret, vx, vy, vz = dhdGetLinearVelocity()
    P = V3D(px, py, pz)
    V = V3D(vx, vy, vz)

    # # Plan: y + 0.02 = 0
    F_total = GeneratePlan(origin=V3D(0, -0.02, 0), position=P, v1=V3D(1, 0, 0), v2=V3D(0, 0, 1), k=2000, c=0)
    
    # # Mur: y + 0.02 = 0
    # F_total = GenerateMur(origin=V3D(0, -0.02, 0), position=P, borne=[-0.02,0.02,-0.2,0.2,-0.02,0.02],v1=V3D(1, 0, 0), v2=V3D(0, 0, 1), k=2000, c=0)
    
    # # Sphere
    # F_total = GenerateSphere(origin=V3D(), position=P, vitesse=V, rayon=0.03, k=2000, c=0)

    # # Cube
    # F_total = GenerateCube(origin=V3D(), position=P, longueur=0.06, v1=V3D(1, 0, 0), v2=V3D(0, 1, 0), k=2000, c=0)

    # # Glissière
    # F_total = GenerateGlissiere(position=P,vitesse=V,k=2000,c=0)

    # # Glissière a clic
    # F_total = GenerateGlissiereAClic(position=P, vitesse=V, omega=2100, k=2000, c=0)

    # # Plan a clic
    # F_total = GeneratePlanAClic(position=P, vitesse=V, omega=2100, k=2000, c=0)

    # # Pivot
    # F_total = GeneratePivot(origin=V3D(), position=P, vitesse=V, longueur=0.03, v1=V3D(1, 0, 0), v2=V3D(0, 1, 0), k=2000)

    # # Tube
    # F_total = GenerateTube(origin=V3D(-0.01,0,0), position=P, vitesse=V, rayon=0.04, hauteur= 0.04, epaisseur=0.02, v1=V3D(0,1,0), v2=V3D(0,0,1),k=2000,c=0)

    [Fx, Fy, Fz] = [F_total.x, F_total.y, F_total.z]
    
    posx = posx + [px]
    posy = posy + [py]
    posz = posz + [pz]

    Forcex = Forcex + [Fx]
    Forcey = Forcey + [Fy]
    Forcez = Forcez + [Fz]

    done = dhdGetButton(0)

    dhdSetForce(Fx, Fy, Fz)

dhdClose()

# figure("my plot")
# plot(posx,'red',posy,'blue',posz,'green')
# show()

figure("Force-Position(x)")
xlabel("x")
ylabel("Forcex")
plot(posx, Forcex)

figure("Force-Position(y)")
xlabel("y")
ylabel("Forcey")
plot(posy, Forcey)

figure("Force-Position(z)")
xlabel("z")
ylabel("Forcez")
plot(posz, Forcez)
show()
# print(max(posx)," et" ,min(posx))


fig = figure("Exemple 3D")
fig3D = fig.gca(projection='3d')

fig3D.scatter(posx, posy, posz, c='r', marker='o')

fig3D.set_xlabel('X Label')
fig3D.set_ylabel('Y Label')
fig3D.set_zlabel('Z Label')

show()
