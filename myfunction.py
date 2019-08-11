import math

arr=[8, 9, 10, 10, 10, 11, 11, 12, 13]

#mean
def mean(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum + int(arr[i])
    #sum=sum(arr)
    mean=sum/len(arr)
    print("Mean :" + str(mean))

#median
def median(arr):
    l=len(arr)
    i=int(l/2)
    if l%2==0:
        median=float((int(arr[i])+int(arr[i+1]))/2)
        print(median)
    else:
        median=arr[i]
        print("Median :" + str(median))

#mode
def mode(arr):
    
    data=set(arr)
    m=list(data)
    for j in range(len(m)):
          x=0
          for i in range(len(arr)):
              if m[j]==arr[i]:
                  x=x+1
          print("Mode of " + str(m[j]) +" : "+ str(x))
             
        
    

#Mid Range
def mr(arr):
    mn=min(arr)
    mx=max(arr)
    mr=(mn+mx)/2
    print("Mid Range : " + str(mr))



#vaariane
def variance(arr):
    import numpy as np
    mean= np.mean(arr)
    nsum=0
    for i in range(len(arr)):
        nsum=nsum + (float((mean-arr[i]))**2)
    variance=nsum/(len(arr))
    print("Variance :" + str(variance))
    

#SD
def sd(arr):
    import numpy as np
    mean= np.mean(arr)
    nsum=0
    for i in range(len(arr)):
        nsum=nsum + (float((mean-arr[i]))**2)
    variance=nsum/(len(arr))
    sd= math.sqrt(variance)
    print("SD = " + str(sd))


'''mean(arr)
median(arr)
mode(arr)
mr(arr)
variance(arr)
sd(arr)'''
