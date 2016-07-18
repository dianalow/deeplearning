"""Softmax."""

import numpy as np

scores = np.array([3.0, 1.0, 0.2])
# scores = np.array([[1, 2, 3, 6],
#                    [2, 4, 5, 6],
#                    [3, 8, 7, 6]])

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    #pass  # TODO: Compute and return softmax(x)
    
    values = np.exp(x);
    return values/np.sum(values,axis=0)
    """
    long method
    
    if len(np.shape(values))>1 :
        values_t =  np.transpose(values)
        for i in xrange(len(values_t):
            values_t[i]=values_t[i]/np.sum(values_t[i])
        return(np.transpose(values_t))
    else:
        return values/np.sum(values)
    """
    
print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
