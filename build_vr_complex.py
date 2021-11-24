# Credit Statement: Borrowed from and inspired by https://notebook.community/gregorjerse/rt2/2015_2016/lab4/Alpha%20shapes%20vs.%20Vietoris%20Rips 

import dionysus as d
import matplotlib.pyplot as plt
import numpy as np
import sys

def get_points(points, indices):
    '''
    Get data from point array on the given indices.
    Useful since simplex spanned by a list of points
    is given as a list of positions of the points
    in a points array.
    '''
    return [points[index] for index in indices]

def draw_triangle(triangle):
    '''
    Draw a triangle on the current figure. 
    Triangle must be given as a list of three 2D points, 
    each point as a list of two numbers.
    '''
    p1, p2, p3 = triangle
    plt.plot([p1[0], p2[0]],[p1[1],p2[1]])
    plt.plot([p1[0], p3[0]],[p1[1],p3[1]])
    plt.plot([p2[0], p3[0]],[p2[1],p3[1]])
    tri = plt.Polygon([[p1[0], p1[1]], [p2[0], p2[1]], [p3[0], p3[1]]])
    plt.gca().add_patch(tri)
        
def draw_line(line):
    '''
    Draw a line on the current figure.
    Line must be given as a list of two 2D points, 
    each point as a list of two numbers.    
    '''
    p1, p2 = line
    plt.plot([p1[0], p2[0]],[p1[1],p2[1]])
    
def draw_point(point):
    '''
    Draw a point on the current figure.
    Point must be given as a list of two numbers.    
    '''
    plt.plot(point)

def draw_simplicial_complex(simplices, points):
    '''
    Draw 2D simplicial complex on the current figure. 
    Input must be a list of simplices, each simplex a
    list of indices in the points array. 
    '''
    handlers = [draw_point, draw_line, draw_triangle]
    for simplex in simplices:
        handlers[len(simplex)-1](get_points(points, simplex))

def rips(points, skeleton, max):
    """
    Generate the Vietoris-Rips complex on the given set of points in 2D.
    Only simplexes up to dimension skeleton are computed.
    The max parameter denotes the distance cut-off value.
    """
    simplices = d.fill_rips(points, skeleton, max)
    return [[vertice for vertice in simplex] for simplex in simplices]

if __name__ == '__main__':
  i = 1
  while i < len(sys.argv):
    # load pointcloud
    filename = sys.argv[i]
    points = np.loadtxt(filename)

    # set epsilion
    radius = 0.1
    if(len(sys.argv) > i+1):
      radius = float(sys.argv[i+1])
      i += 1
    # generate and plot vr complex
    rips_complex = rips(points=points, skeleton=2, max=2*radius)
    draw_simplicial_complex(rips_complex, points)
    plt.scatter(points[:,0], points[:,1])
    plt.show()
    i += 1

    # Code used for processing political data -- ignore for vr computation
    # colors = ['b', 'r', 'g']
    # filename = sys.argv[i]
    # points = np.loadtxt(filename)
    # points_use = points[:,0:2]
    # radius = 0.1
    # if(len(sys.argv) > i+1):
    #   radius = float(sys.argv[i+1])
    #   i += 1
    # rips_complex = rips(points=points_use, skeleton=2, max=2*radius)
    # draw_simplicial_complex(rips_complex, points_use)
    # plt.scatter(points[:,0], points[:,1], c=[points[:,2]%len(colors)])