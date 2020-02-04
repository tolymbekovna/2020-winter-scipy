import numpy as np

# 1
x = np.zeros(10)
x[5] = 1
print('Result null vector of size 10:\n', x)

# 2
x = np.arange(10, 50)
print('\nResult ranging values:\n', x)

# 3
x = x[::-1]
print('\nResult reverse vector:\n', x)

# 4
x = np.arange(0, 9).reshape(3, 3)
print('\nResult 3x3 matrix ranging from 0 to 8:\n', x)

# 5
x = np.array([1, 2, 0, 0, 4, 0])
y = np.nonzero(x)
print('\nResult indices of non-zero elements:\n', y)

# 6
x = np.random.randint(1, 100, (3, 3, 3))
print('\nResult of 3x3x3 array with random values:\n', x)

# 7
x = np.random.randint(1, 100, (10, 10))
_min = x.min()
_max = x.max()
print('\nResult random values 10x10:\n', x)
print('Min: ', _min, '\nMax: ', _max)

# 8
x = np.random.randint(1, 100, 10)
mean = x.mean()
print('\nResult random values of size 10:\n', x)
print('Mean: ', mean)

# 9
x = np.ones((5, 5))
print('\nOriginal array:\n', x)
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print('Bordered array with 0`s:\n', x)

# 10
x = np.zeros((8, 8), dtype=int)
x[1::2, ::2] = 1
x[::2, 1::2] = 1
print('\nCheckerboard pattern:\n', x)

# 11
x = np.random.randint(1, 10, (3, 3))
print('\nOriginal matrix:\n', x)
_min = x.min()
_max = x.max()
x = (x - _min)/(_max - _min)
print('Normalized matrix:\n', x)

# 12
x = np.arange(10)
print('\nOriginal array: ', x)
x[(3 < x) & (x <= 8)] *= -1
print('Negate array: ', x)

# 13
x = np.arange(5)
y = np.arange(10)
print('\nArray 1: ', x)
print('Array 2: ', y)
print('Common values between two arrays: ', np.intersect1d(x, y))

# 14
x = np.zeros((5, 5))
x += np.arange(5)
print('\nMatrix 5x5 with row values ranging from 0 to 4:\n', x)

# 15
x = np.linspace(0, 1, 11, endpoint=False)[1::]
y = np.random.random(10)
print('\nVector of size 10 with values ranging from 0 to 1, both excluded:\n', x)