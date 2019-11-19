import matplotlib.pyplot as plt
import numpy as np
import binascii
from scipy import signal

mapping_table = {
    (0,0,0,0) : -3-3j,
    (0,0,0,1) : -3-1j,
    (0,0,1,0) : -3+3j,
    (0,0,1,1) : -3+1j,
    (0,1,0,0) : -1-3j,
    (0,1,0,1) : -1-1j,
    (0,1,1,0) : -1+3j,
    (0,1,1,1) : -1+1j,
    (1,0,0,0) :  3-3j,
    (1,0,0,1) :  3-1j,
    (1,0,1,0) :  3+3j,
    (1,0,1,1) :  3+1j,
    (1,1,0,0) :  1-3j,
    (1,1,0,1) :  1-1j,
    (1,1,1,0) :  1+3j,
    (1,1,1,1) :  1+1j
}

comparision_table = {
    (0,0,0,0) : 0,
    (0,0,0,1) : 1,
    (0,0,1,0) : 2,
    (0,0,1,1) : 3,
    (0,1,0,0) : 4,
    (0,1,0,1) : 5,
    (0,1,1,0) : 6,
    (0,1,1,1) : 7,
    (1,0,0,0) : 8,
    (1,0,0,1) : 9,
    (1,0,1,0) : 10,
    (1,0,1,1) : 11,
    (1,1,0,0) : 12,
    (1,1,0,1) : 13,
    (1,1,1,0) : 14,
    (1,1,1,1) : 15
}

M=16
Bits_per_symbol=np.log2(M)
Order=pow(2,Bits_per_symbol)
#print ("Ld=",Ld)
#print ("Lb=",Lb)
if M != Order:
   print("the value of M is only acceptable if log2(M)is an integer")

input_bit_arr = np.array([1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0])
no_bits = np.size(input_bit_arr)
bit_period = pow(10,-6)
bit = np.empty(0)

for i in range(len(input_bit_arr)):
    if  input_bit_arr[i] == 1:
        seq = np.ones(100, dtype=int)
    else:
        seq = np.zeros(100, dtype=int)
    bit = np.append(bit,seq)

#print(bit[201],bit[199])
#print(len(bit))
#print(bit_period)

t = np.arange(bit_period/100, (100*bit_period*len(input_bit_arr))/100, bit_period/100)
t = np.append(t,16*bit_period/100)
#print(len(t))
plt.plot(t, bit, 'b+')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title( 'a digital signal' )
plt.show()



data_reshape = np.reshape(input_bit_arr, (int(np.log2(M)), int(no_bits/np.log2(M))))
print(data_reshape)

l = (int(np.log2(M)),1)
value = np.zeros(l,dtype=int)
#print(value)
value_temp = 0

for i in range(int(np.log2(M))):
    value_temp = 0
    for j in range(int(no_bits/np.log2(M))):
       # print(data_reshape[i,j])
       value_temp = value_temp + pow(2 ,(int(no_bits/np.log2(M))-j-1)) * data_reshape[i,j]
        #print(pow(2 ,(int(no_bits/np.log2(M))-j-1)) * data_reshape[i,j])
    value[i,0] = value_temp
print(value)

Real_part = np.zeros(l,dtype=int)
Imaginary_part = np.zeros(l,dtype=int)



for i in range(int(np.log2(M))):
    for b3 in [0, 1]:
        for b2 in [0, 1]:
            for b1 in [0, 1]:
                for b0 in [0, 1]:
                    B = (b3, b2, b1, b0)
                    C   = (b3, b2, b1, b0)
                    #print(B)
                    Q = mapping_table[B]
                    Q1 = comparision_table[C]
                    if value[i,0] == Q1:
                        Real_part[i,0] = Q.real
                        Imaginary_part[i,0] = Q.imag
                        plt.plot(Real_part[i,0], Imaginary_part[i,0], 'bo')
                        plt.text(Real_part[i,0], Imaginary_part[i,0] + 0.2, "".join(str(x) for x in B), ha='center')

print(Real_part)
print(Imaginary_part)
plt.show()
