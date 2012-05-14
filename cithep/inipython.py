def inipython():
#check if in ipython session
    try:
        __IPYTHON__
        return True
    except:
        return False