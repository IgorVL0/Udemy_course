any = True
i = 0
import numpy as np

while any:
    i += 1
    if i == 5:
        any = False
    else:
        print(f'{i} não é igual a 5 ainda')

print(i)

"""
for i in np.arange(0,10):
    print(i)
"""
