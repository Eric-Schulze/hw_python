from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

np.set_printoptions(precision=5, suppress=True) #suppress scientific notation

#generate two clusters of data a(size)=100, b(size)=50

np.random.seed(4711) #change to different prime if needed

a = np.random.multivariate_normal([10,0], [[3,1],[1,4]], size=[100])
b = np.random.multivariate_normal([0,20], [[3,1],[1,4]], size=[50])
x = np.concatenate((a,b),)

print(x.shape)
plt.scatter(x[:,0], x[:,1])
#plt.show()


z = linkage(x, 'single') #try complete, average, ward
'''
Matrix z:
[idx1, idx2, distance, sample_count]
this refers to the cluster formed in iteration z(idx - len(x)) 
'''

print(z)

#cophenetic correlation coefficient
#correlation between cluster and original values
#if CCC is close to 1, the clustering better preserves the original distances

c, coph_dists = cophenet(z, pdist(x))
print(c)

#generate dendrogram
plt.figure(figsize=(15,10))
plt.title('Hierarchical Cluster Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distances')
dendrogram(z, leaf_rotation=90., leaf_font_size=8.,)
plt.show()
