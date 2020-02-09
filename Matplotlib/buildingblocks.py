import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

mpl.interactive(True)
plt.ion()
mpl.is_interactive()

import numpy as np
fig, ax = plt.subplots()
row_vector = np.array([1, 3])
ax.quiver(row_vector)