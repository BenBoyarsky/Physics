#projecile motion on flat ground with numerical methods
#potential updates: return final velocity vector; return final angle; calculate g based on height, not fixed;
#                   add multiple types of objects (This has to be a different update because effective surface area 
#                   changes with an objects angle in the air);
#                   Option for 3D; units;add visualizer;
#                   Variable g; ensure correct parameters are given; Have different methods for different levels of
#                   customization. i.e. have a simple kinematics simulation, one that has variable g, one with aerodynamics, etc
#                   variable tstep; ask user which graphs they want after each sim



import numpy as np
import matplotlib.pyplot as plt
import sys

def final_pos(initial_speed, angle, height, aerodynamics, m, Cd, p, r):
    if initial_speed < 0:
        angle += np.pi
    if height == 0:
            height = sys.float_info.min
    errors = ''
    if height < 0: 
        errors += 'Height cannot be negative.\n'
    if not height > sys.float_info.min and (angle >= np.pi) | (angle <= 0):
        errors += 'Angle must be between 0 to 180 degrees, exclusive.\n'
    if not isinstance(aerodynamics, bool):
        errors += "Aerodynamics must be 'True' or 'False'.\n"
    if m < 0:
        errors += 'Object mass cannot be negative.\n'
    if Cd < 0:
        errors += 'Coefficient of drag cannot be negative.\n'
    if p < 0:
        errors += 'Density cannot be negative.\n'
    if r < 0:
        errors += 'Radius cannot be negative.\n'
    if errors:
        raise ValueError(errors)
    v = np.array([initial_speed * np.cos(angle), initial_speed * np.sin(angle)])
    g = np.array([0, -9.80665])
    pos = np.array([0., height])
    tstep = 0.0001
    t = 0
    Ymax = height
    tmax = 0
    t_arr = []
    x_arr = []
    y_arr = []
    if not aerodynamics:
        while pos[1] > 0:
            pos += v * tstep
            v += g * tstep
            t += tstep
            t_arr.append(t)
            x_arr.append(t)
            y_arr.append(pos[1])
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
            t_arr.append(t)
            x_arr.append(t)
            y_arr.append(pos[1])
            if pos[1] > Ymax:
                Ymax = pos[1]
                tmax = t

    if __name__ == '__main__':
        print(f'Horizontal Displacement: {pos[0]}\nTime: {t}\nFinal Speed {np.linalg.norm(v)}\nMax Height: {Ymax}\nTime to Max: {tmax}')
    else:
        return [pos[0], t, np.linalg.norm(v), Ymax, tmax]

def main(i):
    print(f'--- Simulation {i} ---')
    while True:
        h = float(input('Initial Height (m): '))
        if h >= 0:
            break
        else:
            print('Height must be positive.')
    while True:
        angle = float(input('Initial Angle (deg): '))
        angle = np.deg2rad(angle) % (2 * np.pi)
        if not h > sys.float_info.min and (angle >= np.pi) | (angle <= 0):
                print('Angle must be between 0 to 180 degrees, exclusive.')
        else:
            break
    speed = float(input('Initial Speed (m/s): '))
    while True:
        aerodynamics = input('Aerodynamics using a Sphere (Y/N): ')
        if aerodynamics == 'Y':
            aerodynamics = True
            break
        elif aerodynamics == 'N':
            aerodynamics = False
            break
        else:
            print("Must enter 'Y' or 'N'.")
    if aerodynamics:
        while True:
            m = float(input('Object Mass (kg): '))
            if m > 0:
                break
            else:
                print('Object mass must be positive.')
        while True:
            r = float(input('Radius (cm): '))
            if r > 0:
                break
            else:
                print('Radius must be positive.')
        while True:
            custom = input('Custom Aerodynamics (Y/N): ')
            if custom == 'Y':
                custom = True
                break
            elif custom == 'N':
                custom = False
                break
            else:
                print("Must enter 'Y' or 'N'.")
        if custom:
            while True:
                Cd = float(input('Coefficient of Drag (Based on Projected Area): '))
                if Cd > 0:
                    break
                else:
                    print('Coefficient of drag must be positive.')
            while True:
                p = float(input('Air Density (kg/m^3): '))
                if p > 0:
                    break
                else:
                    print('Air Density must be positive.')
        else:
            Cd = 0.47
            p = 1.13 #LA in the summer
    else:
        m = 0
        Cd = 0
        p = 0
        r = 0
        
    final_pos(speed, angle, h, aerodynamics, m, Cd, p , r / 100)
    while True:
        repeat = input('Run Another Simulation (Y/N): ')
        if repeat == 'Y':
            repeat = True
            break
        elif repeat == 'N':
            repeat = False
            break
        else:
            print("Must enter 'Y' or 'N'.")

    if repeat:
        print()
        main(i+1)
    else:
        print('Quit Program.')

if __name__ == '__main__':
    main(1)