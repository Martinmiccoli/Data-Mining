import numpy as np

def load_npy(filename):
    with open(filename, 'rb') as f:
        return np.load(f)