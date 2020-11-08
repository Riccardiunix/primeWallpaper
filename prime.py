import numpy as np
import math
from multiprocessing import Pool
from PIL import Image

def isPrime(n):
    if n%2 == 0 or n%3 == 0:
        return 0
    for j in range(6, int(math.sqrt(n)+6)):
        if n%(j-1) == 0 or n%(j+1) == 0:
            return 0
    
    return n-1

arr = np.full((1366*768), 40, np.uint8)
cprime = 128
arr[1] = cprime    #2
arr[2] = cprime    #3
arr[4] = cprime    #5
arr[6] = cprime    #7

pool = Pool()
a = pool.map(isPrime, range(1, (1366*768) + 1, 2))

for i in a:
    if (i > 0):
        print(i+1)
        arr[i] = cprime

arr= np.reshape(arr, (768, 1366))
im = Image.fromarray(arr)
im.save("prime_spiral.jpeg")