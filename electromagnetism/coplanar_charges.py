#coplanar_charges (unfinished)

#update: Change charge name to something else, and fix all the places that mentions it;
#        Checker for well-formed codes; allow user to input a charge at a position and
#        visualize its path

import numpy as np
import matplotlib.pyplot as plt
import ast

k = 8.99e9
class charge:
    def __init__(self, m, q, pos):
        self.mass = m
        self.charge = q
        self.pos = pos
        self.velocity = np.array([0, 0])

    def update_pos(self, tstep):
        self.pos += self.velocity * tstep

    def update_velocity(self, tstep, F):
        self.velocity += (F / self.mass) * tstep

    def force(self, other_charge):
        r = other_charge.pos - self.pos
        if np.linalg.norm(r) == 0:
            return 0
        F = -((k * self.charge * other_charge.charge) / (np.linalg.norm(r) ** 3)) * r
        return F

def n_body_problem(charges, t): #unfinished
    plt.ion()
    tstep = 0.001
    n = int(t / tstep)
    for _ in range(n):
        F = np.zeros(len(charges))
        for i in range(len(charges)):
            charges[i].update_pos(tstep) 
            for j in range(len(charges)):
                F[i] += charges[i].force(charges[j])
        for i in range(len(charges)):
            charges[i].update_pos(tstep)
            charges[i].update_velocity(tstep, F[i])

def simulate(test_charge, charges, time):
    tstep = 0.001
    n = int(time / tstep)
    for _ in range(n):
        test_charge.pos += test_charge.velocity * tstep
        F = test_charge.charge * Efield(test_charge.pos, charges)
        test_charge.update_velocity(tstep, F)

def Efield(pos, charges):
    vector = np.zeros(2)
    for point_charge in charges:
        r = pos - point_charge.pos
        vector[0] += ((k * point_charge.charge) / np.linalg.norm(r) ** 2) * (r[0] / np.linalg.norm(r))
        vector[1] += ((k * point_charge.charge) / np.linalg.norm(r) ** 2) * (r[1] / np.linalg.norm(r))
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
                    U[j][i] += ((k * point_charge.charge) / np.linalg.norm(r) ** 2) * (r[0] / np.linalg.norm(r))
                    V[j][i] += ((k * point_charge.charge) / np.linalg.norm(r) ** 2) * (r[1] / np.linalg.norm(r))

    fig, ax = plt.subplots()
    ax.quiver(X, Y, U, V, angles = 'xy')
    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()

def charge_creator(n):
    charges = []
    for i in range(n):
        print(f'--- Charge {i + 1} ---')
        m = float(input('Mass: '))
        q = float(input('Charge: '))
        pos = np.array(ast.literal_eval(input('Position [x, y]: ')))
        print()
        charges.append(charge(m, q, pos))
    return charges

def decipher(code):
    #well-formed code (DO NOT INCLUDE '#'):
    #m1_q1_[x1,y1]_m2_q2_[x2,y2]_..._mn_qn_[xn,yn]
    #Examples:
    # 1 charge
    #1_1_[0,0]

    # 2 charges
    #1_1_[0,0]_1_-1_[1,0]

    # 3 charges
    #1_1_[0,0]_2_-1_[1,1]_0.5_3_[-1,2]

    # 4 charges arranged around the origin
    #1_1_[1,1]_1_-1_[-1,1]_1_1_[-1,-1]_1_-1_[1,-1]

    # Different masses and fractional charges
    #0.1_2.5_[0,0]_0.5_-3.2_[2,-1]_2_1.5_[-3,4]

    # Negative coordinates
    #1_1_[-5,-5]_2_-2_[-2,3]_3_4_[4,-1]

    # Charges along the x-axis
    #1_1_[-3,0]_1_-1_[-1,0]_1_-1_[1,0]_1_1_[3,0]

    # Charges along the y-axis
    #1_1_[0,-3]_1_-1_[0,-1]_1_-1_[0,1]_1_1_[0,3]

    # Asymmetric arrangement
    #2_3_[1,4]_0.5_-2_[-3,1]_4_1_[2,-2]_1_-4_[-1,-3]

    # Larger system: 6 charges
    #1_1_[-3,2]_2_-1_[0,4]_0.5_2_[3,2]_1_-2_[3,-2]_3_1_[0,-4]_2_-1_[-3,-2]
    line = code.split('_')
    m = []
    q = []
    pos = []
    while len(line) > 0:
        pos.append(ast.literal_eval(line.pop()))
        q.append(float(line.pop()))
        m.append(float(line.pop()))
    charges = []
    for i in range(len(m)):
        charges.append(charge(m[i], q[i], pos[i]))
    return charges


def main():
    code = input('Do you have a code? (Y/N): ')
    if code == 'Y':
        line = input('Code: ')
        charges = decipher(line)
        EfieldGraph(charges)


    elif code == 'N':
        n = int(input('Number of Charges: '))
        charges = charge_creator(n)
        EfieldGraph(charges)

if __name__ == '__main__':
    main()