#projecile motion on flat ground with numerical methods
#potential updates: return final velocity vector; return final angle; calculate g based on height, not fixed;
#                   add aerodynamics assuming a spherical object; add multiple types of objects (This has to
#                   be a different update because effective surface area changes with an objects angle in the air);
#                   3D instead of 2D; units; make final_pos() only return, and main() will print; add visualizer;
#                   Variable g; ensure correct parameters are given; Have different methods for different levels of
#                   customization. i.e. have a simple kinematics simulation, one that has variable g, one with aerodynamics, etc
#                   Default values so you dont have to input aerodynamic variables; variable tstep; instead of
#                   raising errors, have the user enter another valid answer;



import numpy as np
import sys

def final_pos(initial_speed, angle, height, aerodynamics, m, Cd, p, r):
    angle = np.deg2rad(angle)
    if height < 0: 
        raise ValueError('Height cannot be negative.')
    if not height > sys.float_info.min:
        if (angle >= np.pi) | (angle <= 0):
            raise ValueError('Angle must be between 0 to 180 degrees, exclusive.')
    v = np.array([initial_speed * np.cos(angle), initial_speed * np.sin(angle)])
    g = np.array([0, -9.80665])
    if height == 0:
        height = sys.float_info.min
    pos = np.array([0., height])
    tstep = 0.0001
    t = 0
    Ymax = height
    tmax = 0
    if not aerodynamics:
        while pos[1] > 0:
            pos += v * tstep
            v += g * tstep
            t += tstep
            if pos[1] > Ymax:
                Ymax = pos[1]
                tmax = t
    else:
        K = -1/2 * Cd * p * (np.pi * r ** 2)
        while pos[1] > 0:
            pos += v * tstep
            Fg = m * np.array([0, -9.80665])
            Fd = K * np.linalg.norm(v) * v
            F = Fg + Fd
            a = F / m
            v += a * tstep
            t += tstep
            if pos[1] > Ymax:
                Ymax = pos[1]
                tmax = t

    if __name__ == '__main__':
        print(f'Horizontal Displacement: {pos[0]}\nTime: {t}\nFinal Speed {np.linalg.norm(v)}\nMax Height: {Ymax}\nTime to Max: {tmax}')
    else:
        return [pos[0], t, np.linalg.norm(v), Ymax, tmax]

def main(i):
    print(f'--- Simulation {i} ---')
    h = float(input('Initial Height (m): '))
    angle = float(input('Initial Angle (deg): '))
    speed = float(input('Initial Speed (m/s): '))
    aerodynamics = input('Aerodynamics using a Sphere (Y/N): ')
    if aerodynamics == 'Y':
        aerodynamics = True
    elif aerodynamics == 'N':
        aerodynamics = False
    else:
        raise ValueError("Must enter 'Y' or 'N'")
    if aerodynamics:
        m = float(input('Object Mass (kg): '))
        r = float(input('Radius (cm): '))
        custom = input('Custom Aerodynamics (Y/N): ')
        if custom == 'Y':
            Cd = float(input('Coefficient of Drag (Based on Projected Area): '))
            p = float(input('Air Density (kg/m^3): '))
        elif custom == 'N':
            Cd = 0.47
            p = 1.13 #LA in the summer
        else:
            raise ValueError("Must enter 'Y' or 'N'")
    else:
        m = 0
        Cd = 0
        p = 0
        r = 0
        
    final_pos(speed, angle, h, aerodynamics, m, Cd, p , r / 100)
    repeat = input('Run Another Simulation (Y/N): ')
    if repeat == 'Y':
        print('\n')
        main(i+1)
    elif repeat == 'N':
        print('Quit Program.')
    else:
        raise ValueError("Must enter 'Y' or 'N'")

if __name__ == '__main__':
    main(1)