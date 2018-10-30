import numpy as np
from numpy import cos, sin

def calc_lambda(s, r, a):
  h = (s + r) * np.exp(-a * 1j) + (1 - 2 * r - s) + r * np.exp(a * 1j)
  hm = np.real(h) ** 2 + np.imag(h) ** 2
  x, y = s, r
  return hm

def build_plot(points):
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib.pyplot as plt
  from matplotlib import cm
  from matplotlib.ticker import LinearLocator, FormatStrFormatter
  import numpy as np
  import matplotlib.pyplot as plt
  from matplotlib.colors import ListedColormap
  cmap_bold = ListedColormap(['#000000', '#ffffff'])
  plt.figure()
  plt.rcParams["figure.figsize"] = list(map(lambda x: x * 1, plt.rcParams["figure.figsize"]))
  for xx, yy in points:
      plt.scatter(xx, yy, c='r',cmap=cmap_bold, linewidths=0, s=5)
  plt.title("Idris 2.0")
  cmin, cmax = -0.1, 1.5
  plt.xlim(cmin, cmax)
  plt.ylim(cmin, cmax)
  plt.xlabel('s')
  plt.ylabel('r')
  plt.plot(0, cmin, 0, cmax, c='k')
  plt.plot(cmin, 0, cmax, 0, c='k')
  plt.grid()
  plt.show()

a, b = -50, 50
points = []
for s in np.arange(0, 1.1, 0.005):
  for r in np.arange(0, 0.6, 0.005):
    for m in range(1, 100):
      alpha = 2 * np.pi * m / (b - a)
      if calc_lambda(s, r, alpha) > 1:
        break
    else:
      points.append((s, r))

build_plot(points)
