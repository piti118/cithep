def dp(o):
    try:
        __IPYTHON__
        from IPython.core.display import display
        display(o)
    except:
        print 'here'
        print o

def inipython():
#check if in ipython session
    try:
        __IPYTHON__
        return True
    except:
        return False
    
def initMPL():
    if not inipython():
        try:
            import matplotlib
            matplotlib.use('Agg')
        except:
            pass
    