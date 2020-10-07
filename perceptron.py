import numpy as np;

s = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
    [1, 1, 1],
])

def learn_basic (input, alpha, theta):
    weights = np.random.rand(1,2)
    xn = [x[0:2] for x in input]
    dn = [x[2] for x in input]

    error = True
    while error:
        error = False
        for i, x in enumerate(xn):
            z = np.sum(xn[i] * weights)
            a = unipolar(z, theta)
            err = dn[i] - a
            error = False if err == 0 else True
            weights = []

def unipolar(z, theta):
    return 1 if z > theta else 0
        