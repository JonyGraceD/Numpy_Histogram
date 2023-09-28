
import matplotlib
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
#2_D numpy array
a=np.array([[0.3,0.5,0.2,0.6,0.7,0.8,0.9],[2,4,5,6,7,8,9]])
f=pd.DataFrame(a)
l=f.loc[0,1]
print(l)
f.plot(kind='hist')
plt.show()

