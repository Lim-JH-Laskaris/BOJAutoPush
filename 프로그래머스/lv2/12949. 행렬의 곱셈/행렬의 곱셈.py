import numpy as np

solution = lambda arr1, arr2 : list(map(lambda x :list(map(int,x)),np.array(arr1)@np.array(arr2)))
    