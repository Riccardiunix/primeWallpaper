import numpy as np
import math
from multiprocessing import Pool
from PIL import Image

def isPrime(n):
    for j in range(6, int(math.sqrt(n)+6)):
        if n%(j-1) == 0 or n%(j+1) == 0:
            return 0    
    return n

if '__main__' == __name__:
    w = 1920
    h = 1080
    n = w*h
    
    fg = 128
    bg = 40
    
    arr = np.full((n), bg, np.uint8)
    for i in [0,1,2,4,6]:
        arr[i] = fg
    
    array = []
    i = 6
    while i < n:
        array.append(i-1)
        array.append(i+1)
        i += 6
    if i == n:
        array.append(i-1)
    if array[-1] > n:
        array + array[:-1]
    
    pool = Pool(4)
    for i in  pool.map(isPrime, array):
        if (i > 0):
            arr[i-1] = fg

    arr = np.reshape(arr, (h, w))
    im = Image.fromarray(arr)
    im.save("prime_spiral.png")