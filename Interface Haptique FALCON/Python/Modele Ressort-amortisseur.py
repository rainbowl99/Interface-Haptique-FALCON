import numpy as np
import matplotlib.pyplot as plt

# Paramètres du système ressort-amortisseur
m = 1.0  # Masse
k = 10.0 # Constante de ressort
c = 0.5  # Coefficient d'amortissement

# Conditions initiales
x0 = 0.0    # Position initiale
v0 = 1.0    # Vitesse initiale
t0, tf = 0, 10 # Intervalle de temps
dt = 0.01   # Pas de temps

# Temps
t = np.arange(t0, tf, dt)

# Initialisation des tableaux de position et de vitesse
x = np.zeros(len(t))
v = np.zeros(len(t))
x[0], v[0] = x0, v0

# Résolution de l'équation du mouvement par la méthode d'Euler
for i in range(1, len(t)):
    a = -(k/m) * x[i-1] - (c/m) * v[i-1]
    x[i] = x[i-1] + v[i-1] * dt
    v[i] = v[i-1] + a * dt

# Tracé des graphiques position-temps et force-temps
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Courbe position-temps')
plt.xlabel('Temps (secondes)')
plt.ylabel('Position (mètres)')

plt.subplot(2, 1, 2)
plt.plot(t, -k*x-c*v)
plt.title('Courbe force-temps')
plt.xlabel('Temps (secondes)')
plt.ylabel('Force (newtons)')

plt.tight_layout()
plt.show()
