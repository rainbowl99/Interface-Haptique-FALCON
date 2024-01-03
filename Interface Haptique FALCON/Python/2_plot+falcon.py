#!/usr/bin/env python3

from pyDhd import *
# bibliothèque numeric pour math
from utils import Vecteur3d as V3D
from utils import *
# bibliothèque plot etc.
# from pylab import *
import numpy as np
from math import sin, cos

done = False

dhdOpen()

# def Create_Plan(O=V3D(), P=V3D(), v1=V3D(), v2=V3D()):
#     Norm = (v1 * v2).norm()
#     OP = P - O
#     distance = OP ** Norm
#
#     Fx = () * (-k * distance.x - c * 0)
#     Fy = (Para[0] * px + Para[1] * py + Para[2] * pz + Para[3] < 0) * (-k * distance.y - c * vy)
#     Fz = (Para[0] * px + Para[1] * py + Para[2] * pz + Para[3] < 0) * (-k * distance.z - c * 0)
#     return
#
#
# # def  glissière_a_clic(p=V3D,

posx = list()
posy = list()
posz = list()

Forcex = list()
Forcey = list()
Forcez = list()


def CreateCube(O=V3D(),longueur=1,v1=V3D(),v2=V3D()):
    l = longueur
    n = (v1 * v2).norm()

    # 4 points sur le plan défini par v1 et v2
    # le vecteur P1_P2 est orienté dans la direction du vecteur v1
    # le vecteur P3_P4 est orienté dans la direction du vecteur v2
    P1 = O + l / 2 * n - l / 2 * v1 - l / 2 * v2
    P2 = O + l / 2 * n + l / 2 * v1 - l / 2 * v2
    P3 = O + l / 2 * n - l / 2 * v1 + l / 2 * v2
    P4 = O + l / 2 * n + l / 2 * v1 + l / 2 * v2

    # 4 points sur l'autre plan
    # le vecteur P5_P6 est orienté dans la direction du vecteur v1
    # le vecteur P7_P8 est orienté dans la direction du vecteur v2
    P5 = O - l / 2 * n - l / 2 * v1 - l / 2 * v2
    P6 = O - l / 2 * n + l / 2 * v1 - l / 2 * v2
    P7 = O - l / 2 * n - l / 2 * v1 + l / 2 * v2
    P8 = O - l / 2 * n + l / 2 * v1 + l / 2 * v2

    # Les vecteurs normaux des plans
    n1 = n  # Plan P1P2P3P4
    n2 = v1  # Plan P2P4P6P8
    n3 = -n  # Plan P5P6P7P8
    n4 = -v1  # Plan P1P3P5P7
    n5 = -v2  # Plan P1P2P5P6
    n6 = v2  # Plan P3P4P7P8

    # Verifier que si le point P est à l'extérieur du cube ou non
    OP1 = P1 - O
    OP2 = P2 - O
    OP3 = P3 - O
    OP5 = P5 - O

    d1 = OP1 ** n1
    d2 = OP2 ** n2
    d3 = OP5 ** n3
    d4 = OP1 ** n4
    d5 = OP1 ** n5
    d6 = OP3 ** n6
    distances = [d1, d2, d3, d4, d5, d6]

    F_total = V3D()
    if all(d < 0 for d in distances):
        for d in distances:
            if d < 0:
                F = k * d * n
                F_total += F
    else:
        F_total = V3D()

    return F_total

while not done:

    k = 2000
    c = 0

    ret, px, py, pz = dhdGetPosition()
    ret, vx, vy, vz = dhdGetLinearVelocity()
    P = V3D(px, py, pz)
    V = V3D(vx, vy, vz)

    # # Plan: y + 0.02 = 0
    # v1 = V3D(1,0,0)
    # v2 = V3D(0,0,1)
    # O = V3D(0,-0.02,0)
    # Norm = (v1*v2).norm()
    # OP = P - O
    # distance = OP ** Norm
    # if distance > 0:
    #     F = -k*distance*Norm
    #     [Fx,Fy,Fz] = [F.x,F.y,F.z]
    # else:
    #     [Fx,Fy,Fz] = [0,0,0]

    # Cercle
    # r = 0.02
    # O = V3D(0,0,0)
    # OP = P - O
    # OP_Norm = OP.norm()
    # distance = OP - r*OP_Norm
    # if OP.mod() > r:
    #     Fx = (-k*(distance) - c*V3D(vx,vy,vz)).x
    #     Fy = (-k*(distance) - c*V3D(vx,vy,vz)).y
    #     Fz = (-k*(distance) - c*V3D(vx,vy,vz)).z
    # else:
    #     Fx = Fy = Fz = 0

    # # Cube
    # v1 = V3D(1, 0, 0)
    # v2 = V3D(0, 1, 0)
    # O = V3D(0, 0, 0)
    # l = 1
    #
    # n = (v1 * v2).norm()
    #
    # # 4 points sur le plan défini par v1 et v2
    # # le vecteur P1_P2 est orienté dans la direction du vecteur v1
    # # le vecteur P3_P4 est orienté dans la direction du vecteur v2
    # P1 = O + l / 2 * n - l / 2 * v1 - l / 2 * v2
    # P2 = O + l / 2 * n + l / 2 * v1 - l / 2 * v2
    # P3 = O + l / 2 * n - l / 2 * v1 + l / 2 * v2
    # P4 = O + l / 2 * n + l / 2 * v1 + l / 2 * v2
    #
    # # 4 points sur l'autre plan
    # # le vecteur P5_P6 est orienté dans la direction du vecteur v1
    # # le vecteur P7_P8 est orienté dans la direction du vecteur v2
    # P5 = O - l / 2 * n - l / 2 * v1 - l / 2 * v2
    # P6 = O - l / 2 * n + l / 2 * v1 - l / 2 * v2
    # P7 = O - l / 2 * n - l / 2 * v1 + l / 2 * v2
    # P8 = O - l / 2 * n + l / 2 * v1 + l / 2 * v2
    #
    # # Les vecteurs normaux des plans
    # n1 = n  # Plan P1P2P3P4
    # n2 = v1  # Plan P2P4P6P8
    # n3 = -n  # Plan P5P6P7P8
    # n4 = -v1  # Plan P1P3P5P7
    # n5 = -v2  # Plan P1P2P5P6
    # n6 = v2  # Plan P3P4P7P8
    #
    # # Verifier que si le point P est à l'extérieur du cube ou non
    # OP1 = P1 - O
    # OP2 = P2 - O
    # OP3 = P3 - O
    # OP5 = P5 - O
    #
    # d1 = OP1 ** n1
    # d2 = OP2 ** n2
    # d3 = OP5 ** n3
    # d4 = OP1 ** n4
    # d5 = OP1 ** n5
    # d6 = OP3 ** n6
    # distances = [d1, d2, d3, d4, d5, d6]
    #
    # F_total = V3D()
    # if all(d < 0 for d in distances):
    #     for d in distances:
    #         if d < 0:
    #             F = k * d * n
    #             F_total += F
    # else:
    #     F_total = V3D()

    F_total = CreateCube(O=V3D(),longueur=1,v1=V3D(1,0,0),v2=V3D(0,1,0))
    [Fx, Fy, Fz] = [F_total.x, F_total.y, F_total.z]

    # # Glissière a clic
    # w = 2100
    # # Contrainte sur les axe x et z
    # # Fx = -k*P.x - c*V.x
    # Fz = ((-k*P.z - c*V.z)/abs(-k*P.z - c*V.z)) * 2
    # Fy = 2*(sin(w*P.y))
    # Fx = 2*(sin(w*P.x))

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
