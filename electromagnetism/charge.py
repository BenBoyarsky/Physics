import numpy as np
import matplotlib.pyplot as plt

#updates: chang
k = 8.99e9
class Charge:
    def __init__(self, m, q, pos):
        self.mass = m
        self.q = q
        self.pos = pos
        self.velocity = np.array([0, 0])

    def update_pos(self, tstep):
        self.pos += self.velocity * tstep

    def update_velocity(self, tstep, F):
        self.velocity += (F / self.mass) * tstep

def Efield(pos, charges):
    vector = np.zeros(2)
    for point_charge in charges:
        r = pos - point_charge.pos
        vector[0] += ((k * point_charge.q) / np.linalg.norm(r) ** 2) * (r[0] / np.linalg.norm(r))
        vector[1] += ((k * point_charge.q) / np.linalg.norm(r) ** 2) * (r[1] / np.linalg.norm(r))
    return vector

def EfieldGraph(charges):
    Xmax = charges[0].pos[0]
    Xmin = charges[0].pos[0]
    Ymax = charges[0].pos[1]
    Ymin = charges[0].pos[1]
    for i in range(len(charges)):
        Xpos = charges[i].pos[0]
        Ypos = charges[i].pos[1]
        if Xpos > Xmax:
            Xmax = Xpos
        elif Xpos < Xmin:
            Xmin = Xpos
        if Ypos > Ymax:
            Ymax = Ypos
        elif Ypos < Ymin:
            Ymin = Ypos
    max = Xmax - Xmin
    if Ymax - Ymin > max:
        max = Ymax - Ymin

    if max == 0:
        max = 1
    Xbounds = [Xmin - 0.3*max, Xmax + 0.3*max]
    Ybounds = [Ymin - 0.3*max, Ymax + 0.3*max]

    n = 30
    x = np.linspace(Xbounds[0], Xbounds[1], n)
    y = np.linspace(Ybounds[0], Ybounds[1], n)
    X, Y = np.meshgrid(x, y)
    U = np.zeros_like(X)
    V = np.zeros_like(Y)
    for point_charge in charges:
        for i in range(len(x)):
            for j in range(len(y)):
                pos = np.array([x[i], y[j]])
                charge_pos = point_charge.pos
                r = pos - charge_pos
                if np.linalg.norm(r) > 0:
                    U[j][i] += ((k * point_charge.q) / np.linalg.norm(r) ** 2) * (r[0] / np.linalg.norm(r))
                    V[j][i] += ((k * point_charge.q) / np.linalg.norm(r) ** 2) * (r[1] / np.linalg.norm(r))

    fig, ax = plt.subplots()
    ax.quiver(X, Y, U, V, angles = 'xy')
    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()