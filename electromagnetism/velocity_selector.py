import numpy as np
import matplotlib as plt

class charge:
    def __init__(self, m, q, y, v):
        self.m = m
        self.q = q
        self.pos = np.array[0, y]
        self.v = v

    def update_pos(self, tstep):
        self.pos += self.v * tstep

    def update_velocity(self, F, tstep):
        self.v += (F / self.m) * tstep

    def force(self, E, B):
        Fe = self.q * E
        Fb = self.q * np.cross(self.v, B)
        F = Fe + Fb
        return F

class velocity_selector:
    def __init__(self, length, height, E, B): #update to more precise details about the capacitor like voltage
        self.length = length
        self.height = height
        self.E = E
        self.B = B

    def monoCheck(self, tolerance, charge):
        tstep = 0.001
        upper_bound = (1. + tolerance) * charge.pos[1]
        lower_bound = (1. - tolerance) * charge.pos[1] 
        while charge.pos[0] < self.length:
            charge.update_pos(tstep)
            F = charge.force(self.E, self.B)
            charge.update_velocity(F, tstep)
            if charge.pos[1] > upper_bound or charge.pos[1] < lower_bound:
                return False
        return True

    def checker(self, tolerance, charges):
        checked = []
        for charge in charges:
            checked.append(self.monoCheck(tolerance, charge))
        return checked