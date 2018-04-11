import numpy as np

a = np.array([[1,0,0,0,0,0],
              [0,1,0,0,0,0],
              [0,0,1,0,0,0],
              [0.1,0.2,0.3,0,0.4,0],
              [0.2,0.4,0,0.2,0.2,0],
              [0,1,0,0,0,0]])
print('    TRANSITION MATRIX   ')
print('----------------------------')
print(a)
r = np.array([[.1,.2,.3],[.2,.4,0],[0,1,0]])
q = np.array([[0,.4,0],[.2,.2,0],[0,0,0]])
i = np.array([[1,0,0],[0,1,0],[0,0,1]])
o = np.array([[0,0,0],[0,0,0],[0,0,0]])
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
print('     ***LIMIT TRANSITION MATRIX***')
p_bar = np.array([[1,0,0,0,0,0],
                  [0,1,0,0,0,0],
                  [0,0,1,0,0,0],
                  [0.111,0.111,0,0,0,0],
                  [0.056,0.556,0,0,0,0],
                  [0,0,0,0,0,0]])
print(p_bar)
