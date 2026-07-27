import modern_robotics as mr
import numpy as np


Slist = np.array([[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,-1,-2],[0,0,0]])
M = np.array([[1,0,0,3],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
T = np.array([[-0.585,-0.811,0,0.076],[0.811,-0.585,0,2.608],[0,0,1,0],[0,0,0,1]])
thetalist0 = np.array([np.pi/4,np.pi/4,np.pi/4])
eomg = 0.001
ev = 0.0001

Ans = mr.IKinSpace(Slist,M,T,thetalist0,eomg,ev)
print(Ans)
