import numpy as np

def adagrad_v(gradf, x0, gamma, epsilon1, epsilon, N):
    x = [np.array(x0).reshape(len(x0), 1)]
    v = np.zeros(shape=x[-1].shape)
    G = [np.zeros(shape=x[-1].shape)]
    for k in range(N):
        g = np.asarray(gradf(x[-1]))
        G.append(G[-1] + np.multiply(g, g))
        v = gamma * np.ones(shape=G[-1].shape)/np.sqrt(G[-1] + epsilon1) * g
        x.append(x[-1] - v)
        if np.linalg.norm(g) < epsilon:
            break
    return x, G