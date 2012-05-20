try:
    display
except NameError:
    print 'here'
    global display
    def tmp(x):
        print x
    display = tmp

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
    