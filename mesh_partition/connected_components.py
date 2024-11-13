import igl
import numpy as np
from scipy.sparse import coo_array

# need to use symmetric matrix
I = [0, 1,  2, 3,   3, 4]
J = [1, 0,  3, 2,   4, 3]
V = [1, 1,  1, 1,   1, 1]
A = coo_array((V, (I, J)), shape=(5, 5))

# convert to csr
A = A.tocsr()
print('sparse matrix A:')
print(A)

N, L, K = igl.connected_components(A)
print()
print(f'we find {N} connected components.')

# exclusive scan K to get the start of each connected component
S = np.zeros(N+1, dtype=int)
S[1:] = np.cumsum(K)

for i in range(N):
    print(f'component {i} has {K[i]} vertices:')
    for j in range(S[i], S[i+1]):
        print(f'  {j}', end=' ')
    print()