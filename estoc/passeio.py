import numpy as np
import matplotlib.pyplot as plt
from random import randrange

passeio = lambda x : np.cumsum([randrange(-1, 2, 2) for i in range(x)])

plt.plot(range(900), passeio(900))
plt.plot(range(900), passeio(900))
plt.plot(range(900), passeio(900))
plt.savefig("graphic.png")
