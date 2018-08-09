import numpy as np
import time
import datetime

#d = np.diag((1, 2, 3, 4))
#print(d)
# for i in range(5):
#     #np.random.seed(int(time.clock()*10**7))
#     #a = np.random.rand(5)
#     print(time.time())
#     date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
#     print(date)
#     #print(a)

# a = np.arange(10)
# b = a[::2].copy()
# print(a)
# print(b)
#
# b[0] = 12
# print(a)
# print(b)

# a = np.random.seed(3)
# a = np.random.random_integers(0, 20, 15)
# print(a)
# print((a%3 == 0))
#
# #a[a%3 == 0] = -1
# #print(a)
#
# a = a[(a%3 == 0)]
# print(a)

b = np.arange(0, 100, 10)
print(b[[2, 3, 4, 4, 3, 2]]) # >>>>> numpy tem uma propriedade q utiliza -1 para volta a ordem bem legal.
b[[9,7]] = -100
print(b)
