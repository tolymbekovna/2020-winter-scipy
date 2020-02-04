import numpy as np
#1
V = np.zeros(10)
V[4] = 1
print('\n Task1 \n create null vector OF Size 10 but the fith value which is 1: \n')
print(V)

#2 
V = np.arange(10,50)
print('\n Task2 \n create vector with values RANGING from 10 to 49: \n Vextor V = ')
print(V)

#3 

Vreversed = V[::-1]
print('\n Task3 \n reverse vector V (firt element becomes last) \n Vreversed:',Vreversed)

#4 
print('\n Task4 \n crear matrix 3x3 with values ranging from 0 to 8 \n marix M =')
M = np.arange(0,9)
M = M.reshape(3,3)
print(M)

#5 

a = [1,2,0,0,4,0]
indices = []
for i in a:
    if(i != 0):
        indices.append(i)
print('\n Task5 \n find indices of non-zero elements from [1,2,0,0,4,0] \n\n indices:',indices)

#6

print('\n\n Task6 \n create array 3x3x3 with random values \n\n')
n = 3
RAINT = np.random.randint(-10000,10000,size=(n,n,n))
print('Random integers between -10000 and 10000: \n\n',RAINT)
RA = np.random.rand(n,n,n)
print('\n Random array: \n\n',RA)

#7

n = 10
Arr = np.random.randint(-10000,10000,size=(n,n))
Arrmin = np.amin(Arr)
Arrmax = np.amax(Arr)
print('\n Task7\n create array 10x10 with random values and find minimum and maximum values \n\n Array Arr = ',Arr,'\n\n minimum = ',Arrmin ,'\n maximom = ' ,Arrmax )

#8

n = 30
M = np.random.randint(-1000,1000,size = n)
print('\n Task8 \n create random vector size 30 and find mean \n\n Vector M = ',M)
sum = 0
for i in range(n):
    sum = sum+ M[i]
sum = sum/n
print('\n Mean = ',sum)
mean1 = np.mean(M)
print('\n mean np,mean() = ',mean1)

#9
print('\n\n Task 9 \n how to add border (filled with 0 ) around existing array\n')
ArrPad = np.pad(Arr,pad_width = 1, constant_values = 0)
print('border filled with 0 np.pad()\n', ArrPad)

#10
n = 8
CB = np.zeros((n,n),dtype= int)
CB[1::2,::2] = 1
CB[::2,1::2] = 1

print('\n\nTask10','nxn matix fill Chekboard pattern\n',CB)

#11

n = 5
Matrix = np.random.randint(-10000,10000,size=(n,n))
print('\n\n Task 11 \n normalize 5x5 random matrix\n Marix = \n',Matrix)
Arrmin = np.amin(Matrix)
Arrmax = np.amax(Matrix)
Mrange = Arrmax - Arrmin
Matrix = Matrix / Mrange
print('\n matrix Normalized by range \n' , Matrix)

#12
n = 12
OA = np.arange(n)
for i in range(len(OA)):
    if i>3 and i<8:
        OA[i]=0
print('\n\n Task12\n',OA)

#13
A1 = np.random.randint(0,10,size=10)
A2 = np.random.randint(0,10,size=20)
Intersect = np.intersect1d(A1,A2)
print('\n\nTask 13 \n Find common values between two array \n A1\n',A1,'\n A2 \n',A2,'\n common values \n',Intersect)

#14
n = 5
Mat = np.zeros((n,n),dtype = int)
Mat[:,:] = range(0,5)
print('\n\n Task 14 \n create 5x5 matrix with row values 0 to 5 \n\n',Mat)

#15
n = 10
Vec = np.arange(1/(n+1), 1, 1/(n+1))
print('\n\n Task 15 \n create vector size 10 with values ranging 0 to 1 , both excluded\n\n',Vec,'\nlength of vector:', len(Vec))
