import numpy as np
from envs import jackPay_env
#the decison space
#the value space    qw
value = np.zeros([21,21])

decision = np.array([
    [5,5,5,5,4,4,3,3,3,3,2,2,2,2,2,1,1,1,0,0,0],
    [5,5,5,4,4,3,3,2,2,2,2,1,1,1,1,1,0,0,0,0,0],
    [5,5,5,4,3,3,2,2,1,1,1,1,0,0,0,0,0,0,0,0,0],
    [5,5,5,4,3,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
])
print(decision.shape)