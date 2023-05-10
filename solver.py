"""A solver for the 1D diffusion equation."""
# created on 05/10/23


import numpy as np


np.set_printoptions(formatter={'float': '{: 6.1f}'.format})


def solve1d(concentration, spacing, time_step, diffusivity):
    flux = -diffusivity * np.diff(concentration) / spacing
    concentration[1:-1] -= time_step * np.diff(flux) / spacing
    return concentration
    # operator "minus-equal" or -= represents what is being set in the equation first
    # so in this case "concentration[1:-1]" minus whatever is followed after the '=' sign

    
def _example():
    D = 100
    Lx = 10
    dx = 0.5
    C1 = 500
    C2 = 0
    C = np.empty(Lx)
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx / D / 2.1
    print(C)
    
    for _ in range(1,5):
        C = solve1d(C, dx, dt, D)
        print(C)

if __name__ == "__main__":
    _example()
