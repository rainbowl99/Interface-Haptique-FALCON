# bibliothèque numeric pour math
from utils import Vecteur3d as V3D
from utils import *


# bibliothèque plot etc.


def GeneratePlan(origin=V3D(), position=V3D(), vitesse=V3D(), v1=V3D(), v2=V3D(), k=0, c=0):
    O = origin
    V = vitesse
    P = position

    n = (v1 * v2).norm()
    OP = P - O
    distance = OP ** n
    if distance > 0:
        F = -k * distance * n - c * V
        if F.mod() > 10:
            F = 10 * F.norm()
    else:
        F = V3D()
    return F


def GenerateMur(origin=V3D(), position=V3D(), vitesse=V3D(), v1=V3D(), v2=V3D(), borne=[0,0,0,0,0,0],k=0, c=0):
    O = origin
    V = vitesse
    P = position

    n = (v1 * v2).norm()
    OP = P - O
    distance = OP ** n
    if borne[0] < P.x < borne[1] and borne[2] < P.y < borne[3] and borne[4] < P.z < borne[5]:
        if distance > 0:
            F = -k * distance * n - c * V
            if F.mod() > 10:
                F = 10 * F.norm()
        else:
            F = V3D()
    else:
        F = V3D()
    return F


def GenerateSphere(origin=V3D(), position=V3D(), vitesse=V3D(), rayon=0, k=0, c=0):
    O = origin
    V = vitesse
    P = position
    r = rayon

    OP = P - O
    OP_Norm = OP.norm()
    distance = OP - r * OP_Norm
    if OP.mod() < r:
        F = -k * distance - c * V
        if F.mod() > 10:
            F = 10 * F.norm()
    else:
        F = V3D()
    return F


def GenerateCube(origin=V3D(), position=V3D(), vitesse=V3D(), longueur=0, v1=V3D(), v2=V3D(), k=0, c=0):
    O = origin
    V = vitesse
    P = position
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
    ns = [n1, n2, n3, n4, n5, n6]

    # Verifier que si le point P est à l'extérieur du cube ou non
    P1P = P - P1
    P2P = P - P2
    P3P = P - P3
    P5P = P - P5

    d1 = P1P ** n1
    d2 = P2P ** n2
    d3 = P5P ** n3
    d4 = P1P ** n4
    d5 = P1P ** n5
    d6 = P3P ** n6
    distances = [d1, d2, d3, d4, d5, d6]

    F_total = V3D()
    if d1 <0 and d2 <0 and d3 < 0 and d4 < 0 and d5<0 and d6 <0:
        res = True
    else:
        res = False

    if res:
        d_max = max(distances)
        i = distances.index(d_max)
        F_total = -k * distances[i] * ns[i] - c * V
        if F_total.mod() > 10:
            F_total = 10 * F_total.norm()
    else:
        F_total = V3D()

    return F_total


def GenerateGlissiere(position=V3D(), vitesse=V3D(), k=0, c=0):
    V = vitesse
    P = position
    # Contrainte sur les axe x et y
    Fz = -k * P.z - c * V.z
    if Fz > 10:
        Fz = 10 * Fz / abs(Fz)
    Fy = -k * P.y
    if Fy > 10:
        Fy = 10 * Fy / abs(Fy)
    Fx = 0
    F_total = V3D(Fx, Fy, Fz)
    return F_total


def GenerateGlissiereAClic(position=V3D(), vitesse=V3D(), omega=0, k=0, c=0):
    V = vitesse
    P = position
    # Contrainte sur les axe x et y
    Fz = -k * P.z - c * V.z
    if Fz > 10:
        Fz = 10 * Fz / abs(Fz)
    Fy = -k * P.y - c * V.y
    if Fy > 10:
        Fy = 10 * Fy / abs(Fy)
    Fx = 2 * (sin(omega * P.x))

    F_total = V3D(Fx, Fy, Fz)
    return F_total


def GeneratePlanAClic(position=V3D(), vitesse=V3D(), omega=0, k=0, c=0):
    V = vitesse
    P = position

    if P.z < 0:
        Fz = -k * P.z - c * V.z
        if Fz > 10:
            Fz = 10 * Fz / abs(Fz)
        Fy = 2 * (sin(omega * P.y))
        Fx = 2 * (sin(omega * P.x))
        F_total = V3D(Fx, Fy, Fz)
    else:
        F_total = V3D()
    return F_total


def GeneratePivot(origin=V3D(), position=V3D(), vitesse=V3D(), longueur=0, v1=V3D(), v2=V3D(), k=0, c=0):
    O = origin
    V = vitesse
    P = position
    l = longueur

    n = (v1 * v2).norm()
    OP = P - O
    distance1 = OP ** n  # La distance(scalaire) entre le point et le plan défini.
    F1 = -k * distance1 * n - c * V  # La force contrainte du plan

    v_unit = OP.norm()
    distance2 = OP - l * v_unit  # La distance(type V3D) entre le point et le point original
    F2 = -k * distance2 - c * V  # La force contrainte du pivot

    F_total = F1 + F2
    if F_total.mod() > 10:
        F_total = 10 * F_total.norm()

    return F_total


def GenerateTube(origin=V3D(), position=V3D(), vitesse=V3D(), rayon=0, hauteur=0, epaisseur=0, v1=V3D(), v2=V3D(), k=0,
                 c=0):
    O = origin
    V = vitesse
    P = position
    h = hauteur
    epa = epaisseur
    r1 = rayon - epa
    r2 = rayon

    n = (v1 * v2).norm()

    OP = P - O
    OP_norm = OP.norm()

    OP_proj = OP ** n  # Calculer la longueur de la projection de OP sur l'axe du tube
    P_proj = O + OP_proj * n  # Obtenir la position de la projection de OP sur l'axe du tube
    distance = (P - P_proj).mod()  # Distance entre le point P et l'axe

    if 0 < OP_proj < h:
        if r1 + epa/2 > distance > r1:  # A l'intérieur du tube
            delta_d = distance - r1
            F_total = -k * delta_d * OP_norm - c * V
            if F_total.mod() > 10:
                F_total = 10 * F_total.norm()
        elif r2 > distance > r1 + epa/2:  # A l'extérieur du tube
            delta_d = distance - r2
            F_total = -k * delta_d * OP_norm - c * V
            if F_total.mod() > 10:
                F_total = 10 * F_total.norm()
        else:
            F_total = V3D()
    else:
        F_total = V3D()

    return F_total
