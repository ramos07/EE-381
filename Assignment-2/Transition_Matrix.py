import numpy as np

#creating the array that will store the transitional matrix
a = np.array([[0.3,0.1,0.3,0.3],[0.2,0.35,0,0.45],[0,0,1,0],[0,0,0,1]])
print('TRANSITION MATRIX')
print(a)
#the following matrices have been detached from the transitional matrix
#arrays to hold the R, Q, I, and 0 matrix
r = np.array([[0.3,0.1],[0.2,0.35]])
q = np.array([[0.3,0.3],[0,0.45]])
i = np.array([[1,0],[0,1]])
o = np.array([[0,0],[0,0]])
print('------------------------------------')
#g will hold the I - Q matrix
g = i - q
print('I - Q Matrix')
print(g)
print('------------------------------------')
#f matrix
f = np.linalg.inv(g)
print('Fundamental Matrix for the Transition Matrix ')
print(f)
print('------------------------------------')
#F*R matrix computed
h = f * r
print('F*R Matrix')
print(h)
print('------------------------------------')
#Limit Transition matrix created
print('***LIMIT TRANSITION MATRIX***')
p_bar = np.array([[1,0,0,0],[0,1,0,0],[0.429,0.078,0,0],[0,0.636,0,0]])
print(p_bar)
print('------------------------------------')
#multiply the transition matrix by stable matrix to obtain the final stable matrix
x_bar = np.array([[0.3],[0.3],[0.15],[0.25]])
stable_matrix = a*x_bar
print('***STABLE MARKET SHARE MATRIX*** ')
print(stable_matrix)
