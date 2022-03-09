from time import time
import numpy as np


tic = time.time()

i_squared = [i**3 for i in range(10)]
toc = time.time()

print(f"time elapsed: {toc - tic}")
