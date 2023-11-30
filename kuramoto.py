import numpy as np
import numpy.typing as ty


def kuramoto(omega_i: np.float32, K: ty.NDArray[np.float32], N: np.uint32, theta_i: np.float32, theta_j: ty.NDArray[np.float32]):
    return omega_i + np.sum(K / N * (np.sin(theta_j - theta_i)))


def coupling_matrix(network_model: str, K: np.float32, N: np.uint8):
    match network_model:
        case "lu":
            K_matrix = np.array(
                [[1.0 if i - 1 == j else 0.0 for i in range(N)] for j in range(N)]
            )
        case "lb":
            K_matrix = np.array(
                [
                    [1.0 if i - 1 == j or i + 1 == j else 0.0 for i in range(N)]
                    for j in range(N)
                ]
            )
        case "bu":
            K_matrix = np.array(
                [
                    [1.0 if i - 1 == j or j - i == N else 0.0 for i in range(N)]
                    for j in range(N)
                ]
            )
        case "bd":
            K_matrix = np.array(
                [
                    [
                        1.0 if i - 1 == j or i + j == 1 or j + i == N else 0.0
                        for i in range(N)
                    ]
                    for j in range(N)
                ]
            )
        case _:
            K_matrix = np.array([[1.0 if i != j else 0.0 for i in range(N)] for j in range(N)])

    return K_matrix * K
