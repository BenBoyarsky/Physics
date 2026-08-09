#orbital motion around a fixed planet
#potential updates: user doesn't start from a fixed location; 3D coordinates instead of 2D;
#                   add atmosphere; user may select planets instead of inputting their own parameters;
#                   figure out system for dealing with infinite loops (i.e. user cannot exceed escape v)

import numpy as np
import sys

def final_pos(planet_radius, planet_mass, object_mass, initial_speed, angle, height):
    pass

def main():
    R = float(input('Planet Radius: '))
    M = float(input('Planet Mass: '))
    m = float(input('Object Mass: '))
    v = float(input('Launch Speed: '))
    angle = float(input('Launch Angle: '))
    h = float(input('Initial Height: '))
    final_pos(R, M, m, v, angle, h)

if __name__ == '__main__':
    main()