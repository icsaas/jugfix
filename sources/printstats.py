from statistics import *
import numpy as np
print 'Cover GNF:', np.mean([c.result for c in covers_gnf])
print 'Cover IC100:', np.mean([c.result for c in covers_ic100])

