#!/usr/bin/env python3

# MIT license
#
# Copyright © 2022 Timo Koch
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
import matplotlib

font = {"family": "normal", "weight": "normal", "size": 12}

matplotlib.rc("font", **font)


def velocity(r, t, wo):
    """The analytical solution"""
    r = np.abs(r)  # symmetric profile
    arg = wo * 1j ** (3.0 / 2.0)
    j0 = lambda s: sp.jv(0, s)
    j0Arg = j0(arg)
    complex_value = -(1.0 - j0(r * arg) / j0Arg) * np.exp(t * 1j) / 1j
    return np.real(complex_value)


def velocity_plot(r, t, wo, scaling):
    """Scaled and translated analytical solution for plotting"""
    return (scaling * velocity(r, t, wo) + t) / np.pi * 180


radius = np.linspace(-1.0, 1.0, 200, endpoint=True)
time = np.linspace(0, 2 * np.pi, 25, endpoint=True)

# plot profiles for these Womersley numbers
wo_numbers = [2, 4, 8, 16]
fig, ax = plt.subplots(1, len(wo_numbers) + 1, figsize=(10, 8), sharey=True)

# plot pressure gradient in the first column
ax[0].set_yticks(time / np.pi * 180)
ax[0].set_yticklabels([f"{int(t)}°" for t in time / np.pi * 180])
ax[0].set_xlim([-1, 1])
ax[0].set_xlabel(r"$\partial p / \partial z, \; P' = 1$")
dpt = np.linspace(0, 2 * np.pi, 50, endpoint=True)
ax[0].plot(np.cos(dpt), dpt / np.pi * 180, "k")

# plot velocity profiles in the other columns
for i, wo in enumerate(wo_numbers):
    ax[i + 1].set_yticks(time / np.pi * 180)
    ax[i + 1].set_xlim([-1, 1])
    ax[i + 1].set_title(f"Wo = {wo}")
    ax[i + 1].set_xlabel(r"$r^* = r/R$")
    ax[i + 1].set_xticks(np.linspace(-1, 1, 5))
    ax[i + 1].set_xticklabels(np.abs(np.linspace(-1, 1, 5)))
    for t in time:
        # scaling is arbitrary since we are only plotting the profile
        # so we choose a scale such that the plot looks good
        vel = velocity_plot(r=radius, t=t, wo=wo, scaling=0.6)
        ax[i + 1].plot(radius, vel, "k")

plt.tight_layout(w_pad=0.3)
fig.savefig("womersley.pdf", dpi=600)
plt.show()
