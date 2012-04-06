import numpy as np
from pylab import plot
from matplotlib import pyplot as plt
import __builtin__
from lundtype import LundType
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
    
def grep(s,a):
    return [x for x in a if s in x]

def projection(x,y,weights=None,bins=40,range=None,ax=None):
    if ax is None: ax = plt.gca()
    bin_range = range
    range = __builtin__.range
    if bin_range is None: bin_range = minmax(x)
    if weights is None: 
        weights = np.zeros(len(x))
        weights.fill(1.) 
    edges = np.linspace(bin_range[0],bin_range[1],bins)
    binno = np.digitize(x,edges)
    
    wy = y*weights
    
    tp_mean = np.zeros(bins-1)
    tp_std = np.zeros(bins-1)
    
    for idigi in xrange(1,bins):
        i = idigi-1
        tmp_wy = wy[binno==i]
        tmp_y = y[binno==i]
        w = weights[binno==i]
        sumw = np.sum(w)
        tp_mean[i] = np.sum(tmp_wy)/sumw
        tmp = np.sum(wfg*(tmp_y-tp_mean[i])**2)
        tp_std[i] = np.sqrt(tmp/sumw)
        
    me = mid(edges)
    print len(me),bins
    return ax.errorbar(me,tp_mean,tp_std)
