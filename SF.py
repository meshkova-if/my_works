import numpy as np
#b = np.int16(16)
#print(np.iinfo(b))#Какие минимальное и максимальное числа можно сохранить в 16 бит?
#c = np.int64()
#print(np.iinfo(c))
#n = np.uint64(16)
#print(np.iinfo(n))
z, step = np.linspace(-6,20,60, endpoint=True, retstep=True)
print(step.round(2))