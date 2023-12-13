import kuramoto
import numpy as np
import matplotlib.pyplot as plt

def simulate_kuramoto(K, N=15, tol=0.0001):
    phi_offs = np.arange(0, 2 * np.pi, step=2/N*np.pi)
    K = kuramoto.coupling_matrix("aa", K, N)
    a_vel = np.ones(N) * 2 * np.pi / 360 # Each oscillator completes 
    steps = 0
    limit = 1000
    
    while np.var(phi_offs) > tol and steps < limit:
        # print("variance", np.var(phi_offs))
        # print("phase diffs:", phi_offs)
        for i in range(len(a_vel)):
            phi_offs[i] += kuramoto.kuramoto(
                a_vel[i], K[i], N, phi_offs[i], phi_offs
            )
        steps += 1
    # print("variance", np.var(phi_offs))
    # print("phase diffs:", phi_offs)
    
    return steps

def plot_steps():
    r = np.arange(-5, 5, step=0.1)
    vals = [simulate_kuramoto(i) for i in r] 
    plt.plot(r, vals)
    plt.show()

def derivative(K, h):
    x = simulate_kuramoto(K+h)
    y = simulate_kuramoto(K)
    # print(x)
    # print(y)
    return (x-y)/h

def gradient_descent(K, alpha, tol, limit):
    count = 0

    while count < limit:
        count += 1
        # print(K)
        K_new = K - alpha * derivative(K, 0.1)
        if np.abs(K_new - K) < tol:
            return K
        K = K_new
    return -1
    
    
if __name__ == "__main__":
    N = 3 # set number of oscillators

    phi_offs = np.arange(0, 2 * np.pi, step=2/N*np.pi)
    # phi_offs = np.random.uniform(0, np.pi, N)
    # a_vel = np.random.uniform(0, 2*np.pi, N)
    a_vel = np.ones(N) * 2 * np.pi # Each oscillator completes 

    tol = 0.0001
    
    plot_steps()
    # print(gradient_descent(1.5, 0.001, 0.0001, 1000))
    # print(simulate_kuramoto(2.4))

