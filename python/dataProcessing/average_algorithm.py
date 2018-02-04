
import numpy as np

def reduceSamples(array,N):
    outputArray = []
    outputArray.append(array[0])
    for i in range(1,len(array)):
        if(i%N == 0):
            tempArray = []
            for j in range(0,N):
                tempArray.append(array[i - j])
            outputArray.append(np.mean(tempArray))
    return outputArray



testArray = [0,1,2,3,4,5,6,7,8,9,10,11,2,3,5,7,3,6,3,6,4,4,3,2,33,3,3,3,3,33]

print len(testArray)

print len(reduceSamples(testArray,2))

print reduceSamples(testArray,2)
