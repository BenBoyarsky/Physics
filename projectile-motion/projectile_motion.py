#projecile motion with numerical methods
#info to add:time to max, final velocity vector, final angle
#new updates: have g be calculated at each instance, so height plays a rol;
#             Work radially instead of by height, so that i can use planets instead of floors

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
    g = -9.81
    if height == 0:
        height = sys.float_info.min
    pos = [0, height]
    tstep = 0.0001
    t = 0
    Ymax = height
    while pos[1] > 0:
        pos += v * tstep
        v[1] += g * tstep
        t += tstep
        if pos[1] > Ymax:
            Ymax = pos[1]
    print(f'Horizontal Displacement: {pos[0]}\nTime: {t}\nFinal Speed {np.linalg.norm(v)}\nMax Height: {Ymax}')
    return [pos[0], t, np.linalg.norm(v), Ymax] #update bs in return statemenet
print(final_pos(initial_speed = 10, height = 0, angle = 45))
 #test