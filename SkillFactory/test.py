import numpy as np

a = np.int8(25)

print(a)
print(type(a))


print(np.iinfo(np.int8))
print(np.iinfo(np.int16))
print(np.iinfo(np.int64))

print('a', np.iinfo(a))

b = np.uint8(124)
print(b)
# 124
print(type(b))
# <class 'numpy.uint8'>
print(np.iinfo(b))
# iinfo(min=0, max=255, dtype=uint8)
print(np.iinfo(np.uint64))
print(2**64-1)

print(2**128-1)
# 340282366920938463463374607431768211455

print(np.sctypeDict)
print(len(np.sctypeDict))

print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')