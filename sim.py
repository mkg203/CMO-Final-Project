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
    vals_dict = {i: simulate_kuramoto(i) for i in r} 
    vals = list(vals_dict.values())
    print(min(vals))
    plt.plot(r, vals)
    plt.show()

    vals_dict = [i for i in vals_dict if vals_dict[i] != 1000]
    print(vals_dict)
    
    return np.random.choice(vals_dict)

def derivative(K, h):
    x = simulate_kuramoto(K+h)
    y = simulate_kuramoto(K)
    # print(x)
    # print(y)
    return (x-y)/h

def gradient_descent(K, alpha, tol, limit):
    def approach(K, h):
        count = 0
        while count < limit:
            count += 1
            # print(K)
            fd = derivative(K, h)
            K_new = K - alpha * fd
            # print("KVALS: ", K, K_new)
            if np.abs(K_new - K) < tol or K_new < 0:
                return K
            K = K_new

        return 1000
    
    left = approach(K, 0.1)
    right = approach(K, -0.1)

    if simulate_kuramoto(left) < simulate_kuramoto(right):
        return left
    return right
    
    
if __name__ == "__main__":
    guess = plot_steps()
    print(guess)
    x = gradient_descent(guess, 0.001, 0.0001, 1000) # K, alpha, tol, max iterations
    print(x)
    print(simulate_kuramoto(x))
