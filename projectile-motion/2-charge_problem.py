#n-charge problem

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

def main():
    pass

if __name__ == '__main__':
    main()