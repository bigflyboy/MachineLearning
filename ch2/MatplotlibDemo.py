import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import kNN

fig = plt.figure()
ax = fig .add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
plt.show()