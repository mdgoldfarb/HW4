#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Breif Overview:
#This script's purpose is to take a page matrix from online and finding its page rank through matrix multiplcation and alpha values and summations
#The rank of the matrix should be associated with an eigenvector of the matrix associated with the highest eigenvalue when alpha is 1
#The eigenvector and rank's difference in values should be affected by the alpha value
import numpy as np #import proper libraries
A =np.array([[0, 1, 1, 0, 0, 0],
             [0, 0, 1, 1, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1, 0],
             [0, 1, 0, 1, 0, 1],
             [0, 0, 0, 0, 1, 0]]) #Make the initial array
M=A/A.sum(axis=0) #Normalize the matrix but doing the sum of the column method
r=np.array([1/6,1/6,1/6,1/6,1/6,1/6]) #MaKE THE original r vector
alpha=1 #Alpha parameter
threshold=1e-6 #Proper threshold
while True: #While loop 
    r_prime=alpha*np.dot(M,r)+(1-alpha)*r
    if np.linalg.norm(r_prime-r)<threshold:
        break #Break when the change is less than the threshhold
    r=r_prime
    
r=r/np.sum(r)

eigenvalues, eigenvectors = np.linalg.eig(M)
Mev = eigenvectors[:,np.argmax(np.real(eigenvalues))].real #Eigenvector of M #Make sure the numbers are real because the eigenvalues/vectors can have complex numbers, takes the eigenvector associated with the largest eigenvalue
print("PageRank:", r_prime)
Mev=Mev/np.sum(Mev)  #Normalize the eigenvector to match the rank of the matrix
print("M Eigenvector:", Mev)


# In[2]:


import numpy as np
A1 =np.array([[0, 1, 1, 0, 0, 0],
             [1, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 1, 0],
             [0, 0, 1, 1, 0, 1],
             [0, 0, 0, 0, 1, 0]]) #ANOTHER MATRIX with the same code
M=A1/A1.sum(axis=0)
r=np.array([1/6,1/6,1/6,1/6,1/6,1/6])
alpha=1
threshold = 1e-6
while True:
    r_prime=alpha*np.dot(M,r)+(1-alpha)*r
    if np.linalg.norm(r_prime-r)<threshold:
        break
    r=r_prime
r=r/np.sum(r)
eigenvalues, eigenvectors = np.linalg.eig(M)
Mev = eigenvectors[:,np.argmax(np.real(eigenvalues))].real #Eigenvector of M
print("PageRank:", r_prime)
Mev=Mev/np.sum(Mev) 
print("M Eigenvector:", Mev)


# In[ ]:




