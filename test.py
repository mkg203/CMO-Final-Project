import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import kuramoto

r = 5


def circle(phi, phi_off, offset_x, offset_y, a_vel):
    return np.array(
        [r * np.cos((phi + phi_off + a_vel)), r * np.sin((phi + phi_off + a_vel))]
    ) + np.array([offset_x, offset_y])


def setup():
    def draw_circle(theta):
        return r * np.sin(theta), r * np.cos(theta)

    np.vectorize(draw_circle)

    plt.rcParams["figure.figsize"] = 5, 5
    fig, ax = plt.subplots()
    ax.plot(*draw_circle(np.linspace(0, 2 * np.pi, 100)))
    ax.set_aspect("equal")
    return fig, ax


def draw(N, phi_offs, a_vel, K, fig, ax, offset_xs=[], offset_ys=[]):
    # K = 0.03

    if not offset_xs:
        offset_xs = np.zeros(N)
    if not offset_ys:
        offset_ys = np.zeros(N)

    # amount of points

    points = [ ax.plot(
            *circle(0, phi_offs[i], offset_xs[i], offset_ys[i], a_vel[i]), marker="o"
        )[0]
        for i in range(N)
    ]

    def update(phi):  # , phi_off, offset_x,offset_y):
        # set point coordinates
        # phi = 0
        for i in range(N):
            # WRITE UPDATE PHASE OFFSET FUNCTION HERE
            x, y = circle(phi, phi_offs[i], offset_xs[i], offset_ys[i], a_vel[i])
            points[i].set_data([x], [y])
            phi_offs[i] += kuramoto.kuramoto(
                a_vel[i], K[i], N, phi_offs[i], phi_offs
            )

        return points

    ani = animation.FuncAnimation(
        fig,
        update,
        # fargs=(phi_offs, offset_xs, offset_ys),
        interval=20,
        frames=np.linspace(0, 2*np.pi, 720),
        blit=True,
        repeat=False,
    )

    # ani.save(".\\oscillators.gif", fps=30)
    plt.show()


if __name__ == "__main__":
    N = 15 # set number of oscillators

    # phi_offs = np.arange(0, 2 * np.pi, step=2/N*np.pi)
    phi_offs = np.random.uniform(0, N * np.pi, N)
    a_vel = np.random.uniform(0, 2*np.pi, N)
    # a_vel = np.ones(N) * 2 * np.pi # Each oscillator completes 

    # offset_xs = np.random.uniform(-30, 30, N)
    # offset_ys = np.random.uniform(-30, 30, N)
    
    K = kuramoto.coupling_matrix("bu", 1.1, N)

    draw(N, phi_offs, a_vel / 360, K, *setup())
