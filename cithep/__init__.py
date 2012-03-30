import numpy as np
from pylab import plot
def mid(x):
    return (x[1:]+x[:-1])/2
#plot a function
def plotf(x,f,*arg,**kwarg):
    v = np.vectorize(f)
    return plotv(x,v,*arg,**kwarg)
    
def plotv(x,f,*arg,**kwarg):
    r = x
    if isinstance(x, (tuple)):
        r = np.linspace(x[0],x[1],100)
    return plot(r,f(r),*arg,**kwarg)

def minmax(data):
    #todo: make this 1 pass
    return tuple([np.min(data),np.max(data)])
    
def linspacet(t,n):
    return np.linspace(t[0],t[1],n)
