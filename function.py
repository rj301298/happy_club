import numpy as np
import math
import statistics

arr=[8, 9, 10, 10, 10, 11, 11, 12, 13]

#mean value
def mean(arr):
    mean= np.mean(arr)
    print("mean =" + str(mean))

#median value
def median(arr):
    median = np.median(arr)
    print("median= " + str(median))


#mode value
def mode(arr):
    try:
        mode= statistics.mode(arr)
        print("mode= " + str(mode))
    except:
        print("Mode : Values with similar frequency")


#variance
def variance(arr):
    var= np.var(arr)
    print("Variane = "+str(var))

#standerd Variance
def sd(arr):
    var= np.var(arr)
    std= math.sqrt(var)
    print("Standerd Deviation =" + str(std))

'''mean(arr)
median(arr)
mode(arr)
variance(arr)
sd(arr)'''
