import numpy as np
import matplotlib.pyplot as plt
import time

st = time.time()
dura_lyst = []
unbreaking_lyst = []
durability_start = 1500
unbreaking = 0
for n in range(10**7):
    durability_start = durability_start - 100
    durability_start = durability_start/(unbreaking + 1)
    unbreaking = unbreaking + 1
    durability_start = durability_start*(unbreaking+1)
    if n%1000==0:
        dura_lyst.append(durability_start)
        unbreaking_lyst.append(unbreaking)
    if durability_start < 10:
        break

print(dura_lyst[-1], unbreaking_lyst[-1], unbreaking_lyst[-1]*10)
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
fig = plt.figure()
plt.plot(unbreaking_lyst, dura_lyst)
plt.show()
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


