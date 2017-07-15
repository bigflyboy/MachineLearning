# -*- coding: UTF-8 -*-
import trees

myDat, labels = trees.createDataSet()
print myDat
print trees.calcShannonEnt(myDat)