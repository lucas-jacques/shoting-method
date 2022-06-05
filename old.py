def Euler_old(f, xa, xb, ya, y1a, n):
    h = (xb - xa) / float(n)
    x = xa
    y = ya
    y1 = y1a
    for i in range(n):
        y1 += h * f(x, y, y1a)
        y += h * y1
        x += h
    return y


# plt.plot(x, Lagrange(tirs[0]["x_array"], tirs[0]["y_array"])(x), label='tir'+str(c))
