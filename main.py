import numpy as np

class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

def getPivot(dim):
    return sample_spherical(1, dim)[0]

def createTree(points, dim):
    p = getPivot(dim)
    tree = Node(p)



    return tree

def sample_spherical(npoints, ndim):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec

def findClosest(tree, p):
    return 

def main():
    num_points = 1
    dim = 1_000_000
    points = sample_spherical(num_points, dim)

    tree = createTree(dim)

    for p in points:
        findClosest(tree, p)

if __name__ == "__main__":
    main()
