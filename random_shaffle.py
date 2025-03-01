import numpy as np

def shuffle_data(X, y, seed=None):
    if seed is not None:
        np.random.seed(seed)
    
    indices = np.random.permutation(len(X))
    
    X_new = X[indices]
    y_new = y[indices]
    
    return X_new, y_new
