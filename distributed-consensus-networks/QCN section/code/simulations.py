#%%

import matplotlib.pyplot as plt
from numpy import *
import scipy as sp

def Pmajority(N,r):
    k = ceil(N/2)-1
    p = sp.special.betainc(k+1,N-k,r)
    return p

def logPmajority(N,r):
    p = -log2(Pmajority(N,r))
    return nan_to_num(p)

def Rmajority(N,eps):
    k = ceil(N/2)-1
    r = sp.special.betaincinv(k+1,N-k,eps)
    return r

N = arange(1, 10**4 + 1, 1)
levels = [5, 10, 20, 30, 40, 50, 60]

plt.plot(N,Rmajority(N,2**(-20)))
plt.plot(N,Rmajority(N,2**(-40)))
plt.plot(N,Rmajority(N,2**(-50)))
plt.plot(N,Rmajority(N,2**(-60)))
plt.plot(N,Rmajority(N,2**(-70)))
plt.plot(N,Rmajority(N,2**(-80)))
plt.plot(N,Rmajority(N,2**(-90)))
plt.xscale('log')

print(N)

# fig, ax = plt.subplots()
# CS = ax.contour(X, Y, Z, levels=levels)
# ax.clabel(CS, inline=True, fontsize=10)
# ax.set_title('Title')
# plt.xscale('log')

# plt.show()

# N = arange(1, 10**4 + 1, 1)
# r = linspace(0, 0.5, 1000)
# levels = [5, 10, 20, 30, 40, 50, 60]

# X, Y = meshgrid(N, r)
# Z = logPmajority(X, Y)

# fig, ax = plt.subplots()
# CS = ax.contour(X, Y, Z, levels=levels)
# ax.clabel(CS, inline=True, fontsize=10)
# ax.set_title('Title')
# plt.xscale('log')

# plt.show()



# %%
