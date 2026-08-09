#projecile motion on flat ground with numerical methods
#potential updates: return final velocity vector; return final angle; calculate g based on height, not fixed;

import numpy as np
import sys

def final_pos(initial_speed, angle, height):
    angle = np.deg2rad(angle)
    if height < 0: 
        raise ValueError('Height cannot be negative.')
    if not height > sys.float_info.min:
        if (angle >= np.pi) | (angle <= 0):
            raise ValueError('Angle must be between 0 to 180 degrees, exclusive.')
    v = np.array([initial_speed * np.cos(angle), initial_speed * np.sin(angle)])
    g = -9.80665
    if height == 0:
        height = sys.float_info.min
    pos = np.array([0., height])
    tstep = 0.0001
    t = 0
    Ymax = height
    tmax = 0
    while pos[1] > 0:
        pos += v * tstep
        v[1] += g * tstep
        t += tstep
        if pos[1] > Ymax:
            Ymax = pos[1]
            tmax = t
    if __name__ == '__main__':
        print(f'Horizontal Displacement: {pos[0]},\nTime: {t}\nFinal Speed {np.linalg.norm(v)}\nMax Height: {Ymax}\nTime to Max: {tmax}')
    else:
        return [pos[0], t, np.linalg.norm(v), Ymax, tmax]

def main():
    h = float(input('Initial Height: '))
    angle = float(input('Initial Angle: '))
    speed = float(input('Initial Speed: '))
    final_pos(speed, angle, h)

if __name__ == '__main__':
    main()