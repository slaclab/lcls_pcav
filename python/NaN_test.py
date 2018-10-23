import numpy as np 

blah = [-1, 1, 2]
print np.isnan(np.log(blah))

blah = [np.inf, 0, -1]
print np.isnan(np.divide(blah, 0))
print np.isnan(np.divide(blah, np.inf))
print np.isnan(np.multiply(blah, np.inf))