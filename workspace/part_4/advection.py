#!/usr/bin/env python3

# MIT license
#
# Copyright © 2023 Timo Koch
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
#
# You need Python with numpy and matplotlib installed.
#
#   python3 -m venv venv
#   source venv/bin/activate
#   python3 -m pip install numpy matplotlib
#   python3 advection.py
#
# After you don't need the installation anymore just delete
# the folder venv (virtual Python environment). If you skip the
# first two commands, the packages will be installed system-wide.
# (You might need to use
#   python3 -m pip install --user numpy matplotlib
# or
#   sudo python3 -m pip install numpy matplotlib
# )

import numpy as np
import matplotlib.pyplot as plt

# physical parameters
length = 1.0  # length of domain
velocity = 0.2 # transport speed

# the exact solution, this will be reused as initial solution
# we make this periodic on the interval [0, 1]
def exact_sol(t, x):
    sol = np.zeros_like(x)
    left_shock = velocity*t + 0.2
    left_shock = left_shock - np.floor(left_shock)
    right_shock = velocity*t + 0.6
    right_shock = right_shock - np.floor(right_shock)
    if right_shock > left_shock:
        where = (x < right_shock) & (x > left_shock)
    else:
        where = (x < right_shock) | (x > left_shock)
    sol[where] = 1.0
    return sol

# numerical parameters (spatial)
num_cells = 100 # number of grid cells
dz = length / num_cells  # discretization length (cm)

# numerical parameters (time)
t_start = 0.0
# make sure to choose a time step that is small enough
# to satisfy the CFL condition for explicit time integration
CFL = 0.95
dt = dz*CFL/velocity
t_end = 3.0

# plot params
output_every_n_steps = 2

#####################################
# the physical flux function ########
#####################################
def f(c):
    """Linear advection equation"""
    return velocity*c

#####################################
# numerical flux functions ##########
#####################################
def flux_central(c_left, c_right, c_left_left=None, flux_limiter=None):
    """
    Central numerical flux function (with optional flux limiter)
    c_left_left is only needed when using a flux limiter

    The idea of a flux limiter is that we use a higher order scheme
    if the gradient is smooth and a lower order scheme at discontinuities.
    The way we detect discontinuities is by looking at the gradient.
    The default is to not use a flux limiter (then we can observe the typical
    oscillations of the central scheme at solution discontinuities).
    """
    central = 0.5*(f(c_left) + f(c_right))

    if flux_limiter is not None:
        gradient_bottom = (c_right - c_left) + np.copysign(1e-10, (c_right - c_left))
        gradient_indicator = (c_left - c_left_left)/gradient_bottom
        lower_order = flux_upwind(c_left, c_right)
        return lower_order - flux_limiter(gradient_indicator)*(lower_order - central)
    return central

def flux_lax_friedrichs(c_left, c_right, _=None):
    """
    Lax-Friedrichs numerical flux function (adds artificial diffusion)
    """
    return 0.5*(f(c_left) + f(c_right)) - 0.5*dz/dt*(c_right - c_left)

def flux_upwind(c_left, c_right, _=None):
    """
    Upwind numerical flux function
    Take the information from the left or right depending on the sign of the velocity
    """
    return f(c_left) if velocity >= 0 else f(c_right)

#####################################
# some flux limiters ################
#####################################
def superbee(r):
    return np.maximum(0, np.maximum(np.minimum(2*r, 1), np.minimum(r, 2)))

def vanleer(r):
    absr = np.abs(r)
    return (r + absr)/(1 + absr)

def minmod(r):
    return np.maximum(0, np.minimum(r, 1))

#####################################
# all schemes to run ################
#####################################
# dictionary of names mapping to numerical flux function
schemes = {
    "central": flux_central,
    #"central (superbee)": lambda l, r, ll: flux_central(l, r, ll, flux_limiter=superbee),
    #"central (vanleer)": lambda l, r, ll: flux_central(l, r, ll, flux_limiter=vanleer),
    #"central (minmod)": lambda l, r, ll: flux_central(l, r, ll, flux_limiter=vanleer),
    "Lax-Friedrichs": flux_lax_friedrichs,
    "upwind": flux_upwind,
}

WRITE_PNG_OUTPUT = False

###########################################################################
# the 1d grid: it looks like this: |-|-|-|-|-| with faces (|) and cells (-)
# we will simulate flow from left to right --->
###########################################################################
cell_pos = np.linspace(0.5 * dz, length - 0.5 * dz, num_cells, endpoint=True)

# array of unknowns (initial solution); c in each cell (for each scheme)
concentration = np.zeros(shape=(len(schemes), num_cells))
concentration = np.vstack([exact_sol(0.0, cell_pos),]*len(schemes))

# array of unknowns (new/current time step)
concentration_new = np.copy(concentration)

# prepare matplotlib output
fig, ax = plt.subplots(1, 1, figsize=(5.0, 3.5))
(plot_handle_exact,) = ax.plot(cell_pos, concentration[0], "k-", label="exact", lw=1)
plot_handles = []
for i, label in enumerate(schemes.keys()):
    (plot_handle,) = ax.plot(cell_pos, concentration[i], label=label, lw=2)
    plot_handles.append(plot_handle)
ax.set_ylim([-0.1, 1.5])
ax.set_xlabel("domain extent")
ax.set_ylabel("concentration")
ax.legend(loc="upper center", ncol=2)
fig.tight_layout()

def writeOutput(i):
    """Return true every n time steps"""
    return i % output_every_n_steps == 0

# reserve some memory (avoid allocating memory within loops)
c_left = np.zeros(len(cell_pos)+1)
c_right = np.zeros(len(cell_pos)+1)
c_left_left = np.zeros(len(cell_pos)+1)
F = np.zeros(len(cell_pos)+1)

# sanity check
if velocity < 0.0:
    raise ValueError("This example assumes positive velocities")

#####################################
# time loop and plotting ############
#####################################
png_output_counter = 0
time_points = np.linspace(dt, t_end, int(np.floor(t_end / dt)))
for time_step, t_new in enumerate(time_points):
    t_old = t_new - dt

    # do udpate for every scheme in the list
    for i, numerical_flux in enumerate(schemes.values()):
        # We make two variables c_left and c_right that, for each
        # facet in the grid, store the left and right cell value
        # these are then passed to the flux function F(c_left, c_right)
        # In constructing these, we also provide the boundary conditions:
        # Periodic boundary conditions
        c_left = np.concatenate(([concentration[i,-1],], concentration[i]))
        c_right = np.concatenate((concentration[i], [concentration[i,-1],]))
        # for higher order schemes we need on more cell in upstream direction (v>0)
        c_left_left = np.concatenate(([concentration[i,-2], concentration[i,-1]], concentration[i,0:-1]))

        # evaluate numerical flux functions at all facets
        F = numerical_flux(c_left, c_right, c_left_left)

        # update discrete solution (explicit Euler update)
        concentration_new[i] = concentration[i] - dt / dz * (F[1:] - F[:-1])

        # update plot
        if writeOutput(time_step):
            plot_handles[i].set_data(cell_pos, concentration_new[i])

        # update old solution in preparation for next time step
        concentration[i] = concentration_new[i]

    # update the exact solution and plot
    if writeOutput(time_step):
        print(f"Time step {time_step} done.")
        plot_handle_exact.set_data(cell_pos, exact_sol(t_new, cell_pos))
        plt.pause(1)
        if WRITE_PNG_OUTPUT:
            fig.savefig(f"advection-{png_output_counter:04d}.png", dpi=150)
            png_output_counter += 1

plt.show()
