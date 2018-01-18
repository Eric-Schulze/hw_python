import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn import datasets, cluster
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from sklearn.cluster import AgglomerativeClustering
import numpy as np

'''
#easy way because using imported functions
iris = datasets.load_iris()
x = iris.data

pca = decomposition.PCA(n_components = 3)
pca.fit(x)

x = pca.transform(x)

print(pca.explained_variance_ratio_)

fig = plt.figure(1, figsize=(7,50))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[:,0], x[:,1], x[:,2])
plt.show()
'''

'''
iris = datasets.load_iris()
x_iris = iris.data
y_iris = iris.target
iris = AgglomerativeClustering(n_clusters=3, linkage='ward').fit_predict(x_iris)
print('prediction\n', iris)
print('actual\n', y_iris)
'''

'''
Generate 3D data of 40 sample data points, normal distribution
generate 2 classes of data

sample means:   m-1 = [0,0,0]  m-2 = [1,1,1]

covariance matrix = identity matrix for both groups of data

Why 3D? PCA allows dimension reduction from 3D to 2D

Generate 3x20 datasets, each colomn is a 3D vector
and the data set having form of a 3x20 matrix
'''

np.random.seed(7411)

mu_vec1 = np.array([0,0,0])
mu_vec2 = np.array([1,1,1])
cov_mat = np.array([[1,0,0],[0,1,0],[0,0,1]])
group1 = np.random.multivariate_normal(mu_vec1, cov_mat, 20).T
group2 = np.random.multivariate_normal(mu_vec2, cov_mat, 20).T


#plot two groups
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
plt.rcParams['legend.fontsize'] = 10
ax.plot(group1[0,:], group1[1,:],group1[2,:], 'o', markersize=8, color='blue', alpha=0.5, label='group1')
ax.plot(group2[0,:], group2[1,:],group2[2,:], 'o', markersize=8, color='red', alpha=0.5, label='group2')
plt.title('DataSamplesForGroup1AndGroup2')
ax.legend('loc=upperright')
plt.show()


'''
Need to merge group1 and group2 into 3x40 Matrix
Then we will compute the mean vector of d.dimensions
Then compute the scatter/covariance matrix
Eigenvectors and eigenvalues from the covariance matrix
Select required number of highest eigenvalues and select the corresponding eigenvectors
From those eigenvectors, get the corresponding original data
'''

all_samples = np.concatenate((group1, group2), axis=1)

#Compute mean vector
mean_x = np.mean(all_samples[0,:])
mean_y = np.mean(all_samples[1,:])
mean_z = np.mean(all_samples[2,:])
mean_vector = np.array([[mean_x], [mean_y], [mean_x]])

#compute covariance matrix
cov_mat = np.cov([all_samples[0,:], all_samples[1,:], all_samples[2,:]])
print('Covariance Matrix\n', cov_mat)

eig_val, eig_vec = np.linalg.eig(cov_mat)

print('eigenvector\n', eig_vec)
print('eigenvalue\n', eig_val)

#make list of (eig_val, eig_vec) tuples
eig_pairs = [(np.abs(eig_val[i]), eig_vec[:,i]) for i in range (len(eig_val))]

eig_pairs.sort(key = lambda x: x[0], reverse=True)


#combine the two eig_vec with the highest eig_val to construct a 2D matrix
matrix_w = np.hstack((eig_pairs[0][1].reshape(3,1), eig_pairs[1][1].reshape(3,1)))

print()
print('Reduced Eigenvector Matrix\n',matrix_w)

#use the matrix_w to transfrom all_samples
transformed = matrix_w.T.dot(all_samples)

print()
print(transformed)

plt.plot(transformed[0,0:20], transformed[1,0:20], 'o', markersize=7, color='blue', alpha=0.5, label='group1')
plt.plot(transformed[0,20:40], transformed[1,20:40], '^', markersize=7, color='red', alpha=0.5, label='group2')

plt.show()