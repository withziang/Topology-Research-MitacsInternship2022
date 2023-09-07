import scipy.stats as scip
import statistics as stat
import matplotlib.pyplot as mat
import numpy as np
import math as math


delta = 34.7 - 29.8  
#first data
m = 20
dev_m = 4
#second data
n= 25
dev_n = 5

normal_1 = np.random.normal(delta,math.sqrt((dev_m * dev_m)/n+(dev_n * dev_n)/m),100)
print(scip.ttest_1samp(normal_1, popmean=0))


normal_x = np.random.normal(30,2,1000)
normal_y = np.random.normal(10,3,1000)

mat.hist(normal_x)
mat.hist(normal_y)
mat.hist(normal_x - normal_y)
mat.show()