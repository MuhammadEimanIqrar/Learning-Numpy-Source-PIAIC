# Numpy vs Python:

import numpy as np

l = range(1000000) # Python List
d = np.arange(1000000) # Numpy List

%time for i in range(1,10): r = [x*2 for x in l] # For Python
%time for i in range(1,10): r = d*2 # For Numpy


