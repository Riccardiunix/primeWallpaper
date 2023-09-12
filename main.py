import math
import numpy as np
import multiprocessing
from PIL import Image

def isPrime(n):
    for j in range(6, int(math.sqrt(n)+6)):
        if n%(j-1) == 0 or n%(j+1) == 0:
            return 0
    return n

if '__main__' == __name__:
    w = 1366
    h = 768
    n = w*h

    fgg = 192
    fg = 128
    bg = 40

    arr = np.full((n), bg, np.uint8)
    arr[1] = fg
    for i in [0,2,4,6]:
        arr[1] = fgg

    array = []
    i = 12
    while i < n:
        if (i-1) % 5:
            array.append(i-1)
        if (i+1) % 5:
            array.append(i+1)
        i += 6
    if i == n:
        array.append(i-1)
    if array[-1] > n:
        array = array[:-1]

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for i in  pool.map(isPrime, array):
        if (i > 0):
            if (arr[i-3] == fg):
                arr[i-1] = fgg
                arr[i-3] = fgg
            else:
                arr[i-1] = fg

    arr = np.reshape(arr, (h, w))
    im = Image.fromarray(arr)
    im.save("primeWallpaper.png")
