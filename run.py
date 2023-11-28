import numpy as np
import kuramoto
import plot


def driver(N=2):
    N = 15  # set number of oscillators

    # phi_offs = np.arange(0, 2 * np.pi, step=2/N*np.pi)
    phi_offs = np.random.uniform(0, N * np.pi, N)
    # a_vel = np.random.uniform(0, 2*np.pi, N)
    a_vel = np.ones(N) * 0.1

    # offset_xs = np.random.uniform(-30, 30, N)
    # offset_ys = np.random.uniform(-30, 30, N)
    
    K = kuramoto.coupling_matrix("bu", 1.1, N)

    plot.draw(N, phi_offs, a_vel, K, *plot.setup())


def main():
    driver()


if __name__ == "__main__":
    main()
