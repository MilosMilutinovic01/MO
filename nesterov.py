import numpy as np

def nesterov_gradient_descent_v(gradf, x0, gamma, epsilon, omega, N):
    x = [np.array(x0).reshape(len(x0), 1)]
    v = np.zeros(shape=x[-1].shape)
    for k in range(N):
        xpre = x[-1] - omega*v   # x_k prim
        g = gradf(xpre)
        v = omega*v + gamma*g
        x.append(x[-1] - v)
        if np.linalg.norm(g) < epsilon:
            break
    return x