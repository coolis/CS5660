import numpy
import math

x = [9,7,3,5]

def haar(x):
    inputVector = numpy.array(x)    
    n = inputVector.size
    tempVector = numpy.copy(inputVector)
    
    while (n > 1):        
        for i in range(0, n, 2):
            avg = (tempVector[i] + tempVector[i+1]) / 2
            diff = tempVector[i] - avg
            inputVector[i/2] = avg
            inputVector[i/2 + n/2] = diff
        tempVector = numpy.copy(inputVector)      
        n = n/2
        
    return inputVector

def inverse_haar(x):
    inputVector = numpy.array(x)
    n = 1
    tempVector = numpy.copy(inputVector)
    
    while(n < inputVector.size):
        for i in range(0, n):
            avg = tempVector[i]
            diff = tempVector[i+n]
            inputVector[i*2] = avg + diff
            inputVector[i*2+1] = avg - diff
        tempVector = numpy.copy(inputVector)
        n = n*2
        
    return inputVector

print haar(x)      
        

