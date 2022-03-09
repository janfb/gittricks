from time import time

i_squared = []

tic = time.time()
for i in range(10):
    i_squared.append(i**3)
toc = time.time()

print(f"time elapsed: {toc - tic}")
