import matplotlib.pyplot as plt
from numpy.random import rand
arr = ["Americans", "Asians", "European"]
c = 0
for color in ['red', 'blue', 'green']:
    n = 750
    x, y = rand(2, n)
    scale = 200.0 * rand(n)
    ### matplotlib.pyplot function to generate the graph
    plt.scatter(x, y, c=color, s=scale, label=arr[c], alpha=0.3, edgecolors='none')
    c = c+1
plt.legend()
plt.grid(True)
plt.show()