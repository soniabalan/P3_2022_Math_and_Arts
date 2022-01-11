import numpy as np
import matplotlib.pyplot as plt

# Equal aspect ratio Figure with black background and no axes.
fig, ax = plt.subplots(facecolor='k')
ax.axis('equal')
ax.axis('off')

# Colour the lines sequentially from a Matplotlib colormap.
cm = plt.cm.get_cmap('Spectral')

def add_to_plot(lasta, a, n):
    """Add a semi-circular arc from a to lasta.

    Arcs alternate to be above and below the x-axis according to whether
    n is even or odd.

    """

    # Arc centre and radius.
    c, r = (a + lasta) / 2, abs(a - lasta) / 2
    x = np.linspace(-r, r, 1000)
    y = np.sqrt(r**2 - x**2) * (-1)**n
    color = cm(n/max_terms)
    ax.plot(x+c, y, c=color, lw=1)

# Keep track of which numbers have been "visited" in this set.
seen = set()
n = a = 0
lasta = None
max_terms = 62 #60
while n < max_terms:
    lasta = a
    if (b := a - n) > 0 and b not in seen:
        a = b
    else:
        a = a + n
    seen.add(a)
    n += 1
    add_to_plot(lasta, a, n)

plt.show()

def add_to_plot(lasta, a, n):
    c = (a + lasta) / 2
    r = abs(a - lasta) / 2
    x = np.linspace(-r, r, 1000)
    y = np.sqrt(r**2 - x**2) * (-1)**n
    color = cm(n/max_terms)
    X = x+c
    f = np.sqrt(2)
    ax.plot((X-y)*f, (X+y)*f, c=color, lw=1)