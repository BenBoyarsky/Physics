#orbital motion around a fixed planet
#potential updates: user doesn't start from a fixed location; 3D coordinates instead of 2D;
#                   add atmosphere; user may select planets instead of inputting their own parameters;
#                   figure out system for dealing with infinite loops (i.e. user cannot exceed escape v)
#                   units;

import numpy as np
import sys

def final_pos(planet_radius, planet_mass, object_mass, initial_speed, angle, initial_height):
    R = planet_radius
    M = planet_mass
    m = object_mass
    angle = np.deg2rad(angle)
    v = np.array([initial_speed * np.cos(angle), initial_speed * np.sin(angle)])
    h = initial_height
    if h == 0:
        h = sys.float_info.min
    r = np.array([0, R + h])
    G = 6.6743e-11
    g = -((G * M) / np.linalg.norm(r) ** 3) * r
    tstep = 0.001
    t = 0
    t_apoapsis = 0
    apoapsis = np.linalg.norm(r)
    while np.linalg.norm(r) > R:
        r += v * tstep
        g = -((G * M) / np.linalg.norm(r) ** 3) * r
        v += g * tstep
        t += tstep
        if np.linalg.norm(r) > apoapsis:
            apoapsis = np.linalg.norm(r)
            t_apoapsis = t

    if __name__ == '__main__':
        print(f'Final Position: {r}\nFinal Speed: {np.linalg.norm(v)}\nTime: {t}\nApoapsis: {apoapsis}\nTime to Apoapsis: {t_apoapsis}')
    else:
        return [r, v, t, apoapsis, t_apoapsis]
        

    
    

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