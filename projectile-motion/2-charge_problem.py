#n-charge problem

import numpy as np
import matplotlib as plt

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



def simulate(charges, t):
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
        
            
        
        
                


def main():
    pass

if __name__ == '__main__':
    main()