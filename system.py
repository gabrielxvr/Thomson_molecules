import numpy as np
import pandas as pd

# vertices class definition
class P:
    def __init__(self, x, y, z, ind):
        self.position = (x, y, z)
        self.index = ind
        
    def __repr__(self):
        return f'p{self.index+1}'
        
    # distances was setted as the mul function
    def __mul__(self, other):
        return ((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2 + (self.position[2] - other.position[2])**2)**(1/2)

# calculate the distance for all of the particles    
def distances_matrix(vp, dec=1):
    n_rows = np.shape(vp)[0]
    p_list = []
    for i in range(n_rows):
        x = vp[i][0]
        y = vp[i][1]
        z = vp[i][2]
        p_list.append(P(x, y, z, i))
        
    p_row = np.array([p_list])
    p_column = np.array([[i] for i in p_list])

    Dist = p_column @ p_row
    n = Dist.shape[0]
    Dist[range(n), range(n)] = 100
    
    Dist = Dist/Dist.min()
    
    Dist = np.array(Dist, dtype=float)
    
    Dist = np.around(Dist, decimals=dec)
    
    Dist[range(n), range(n)] = 0
    
    return Dist

# computate the system hamiltonian
def hamiltonian(d_array, alpha, beta, gamma, dec=1):
    H_dist = beta*np.e**(gamma*(1 - d_array))
    n = H_dist.shape[0]
    H_dist[range(n), range(n)] = alpha
    
    H_dist = np.array(H_dist, dtype=float)

    H_dist = np.around(H_dist, decimals=1)
    
    return H_dist
        