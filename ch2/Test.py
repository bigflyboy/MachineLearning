import kNN

# group, labels = kNN.createDataSet()
#
# print group
# print labels
#
# print kNN.classify0([0, 0], group, labels, 3)

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')

# fig = plt.figure()
# ax = fig .add_subplot(111)
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
# plt.show()

normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
print normMat
print ranges
print minVals
