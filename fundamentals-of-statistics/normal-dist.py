import numpy as np
from scipy.state import norm

x = np.linespace(-4, 4, 100)
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.cdf(x))

