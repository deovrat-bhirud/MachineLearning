import numpy as np
from scipy import stats
n = int(input())
q = [int(i) for i in input().split()]
mean = np.mean(q)
median = np.median(q)
mode = stats.mode(q).mode[0]
sd = np.std(q)
ld = mean - ( 1.96 * sd / np.sqrt(n))
ud = mean + ( 1.96 * sd / np.sqrt(n))
print(mean)
print(median)
print(mode)
print('{0:.1f}'.format(sd))
print('{0:.1f}'.format(ld), '{0:.1f}'.format(ud))
