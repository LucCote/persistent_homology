import dionysus as d
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import pandas

# number of homologies to computer
homology_dim = 3
# max epsilon of vr complex to comopute
max_r = 1

# plots barcodes given barcode data
def plot_bars(dgm, order='birth', show=False, ax=None, **bar_style):
  bar_kwargs = {'color': 'b'}
  bar_kwargs.update(bar_style)

  if order == 'death':
    generator = enumerate(sorted(dgm, key = lambda p: p.death))
  else:
    generator = enumerate(dgm)

  if ax is None:
      ax = plt.axes()

  for i,p in generator:
    if p.death == math.inf:
      ax.plot([p.birth, max_r], [i,i], **bar_kwargs)
    else:
      ax.plot([p.birth, p.death], [i,i], **bar_kwargs)
  ax.set_xlim([0, max_r])
  if show:
    plt.show()

# generates and displays barcodes from given pointcloud
# verbose: prints each barcode if true
# title: sets title of the graph
def generate_barcode(pointcloud, verbose=False, title=''):
  # generate vr sequence
  f = d.fill_rips(pointcloud, homology_dim, max_r)

  # compute homologies for every vr complex in filter
  m = d.omnifield_homology_persistence(f)

  # generate barcode data from computed homologies and vr sequence
  dgms = d.init_diagrams(m, f, 2)
  if verbose:
    for i, dgm in enumerate(dgms):
      for pt in dgm:
        print(i, pt.birth, pt.death)

  # plot data
  fig, axes = plt.subplots(homology_dim)
  fig.suptitle(title)
  for i in range(homology_dim): # generate a plot for each homology group
    plot_bars(dgms[i], show = False, ax=axes[i])
    axes[i].axes.get_yaxis().set_visible(False)
    axes[i].set_title("Homology Group " + str(i))
  plt.tight_layout()
  plt.show()
  return dgms

if __name__ == '__main__':
  i = 1
  while i < len(sys.argv):
    # load pointcloud
    filename = sys.argv[i]
    points = np.loadtxt(filename)

    # set epsilion
    max_r = 1
    if(len(sys.argv) > i+1):
      max_r = float(sys.argv[i+1])
      i += 1
    generate_barcode(points, title="Persistant Homologies of " + filename)
    i += 1

  # Code used for processing political data -- ignore for homology computation
  # data = pandas.read_csv('luc_R_no_stopwords.csv')
  # points = data.values
  # np.savetxt('luc_R_no_stopwords', points)
  # plt.scatter(points[:,0], points[:,1])
  # plt.show()
  # rep = plot_barcode(points, title="Persistant Homologies")

  # data = pandas.read_csv('luc_D_no_stopwords.csv')
  # points = data.values
  # np.savetxt('luc_D_no_stopwords', points)
  # plt.scatter(points[:,0], points[:,1])
  # plt.show()
  # dem = plot_barcode(points, title="Persistant Homologies")

  # data = pandas.read_csv('luc_no_stopwords_labelled.csv')
  # points = data.values
  # for point in points:
  #   point[2] = float(point[2])
  # np.savetxt('luc_no_stopwords_labelled', points)
  # plt.scatter(points[:,0], points[:,1])
  # plt.show()
  # dem = plot_barcode(points, title="Persistant Homologies")

  # print(d.bottleneck_distance(rep[0], dem[0]))
  # print(d.bottleneck_distance(rep[1], dem[1]))
