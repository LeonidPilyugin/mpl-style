#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
# plt.style.use("https://raw.githubusercontent.com/LeonidPilyugin/mpl-style/refs/heads/main/simple.mplstyle")
plt.style.use("simple.mplstyle")

X = np.linspace(-3, 3, 100)
Y1 = X ** 2
Y2 = 3 - X
plt.plot(X, Y1, label="parabola")
plt.plot(X, Y2, label="line")

plt.errorbar(
    [ -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5 ],
    [ 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3 ],
    yerr=[ 0.5 ] * 11,
    label="data",
    fmt=".",
)

plt.title("Plot title")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()

plt.savefig("plot.png")
