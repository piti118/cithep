def dp(o):
    try:
        __IPYTHON__
        display(o)
    except:
        print o

def inipython():
#check if in ipython session
    try:
        __IPYTHON__
        return True
    except:
        print 'here'

        return False
    
def initMPL():
    if not inipython():
        try:
            import matplotlib
            matplotlib.use('Agg')
        except:
            pass
    