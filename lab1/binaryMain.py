import matplotlib.pyplot as plt
from random import sample
from search import binary_search
from time import time
from random import choice
dataToPlot = {
    "index": [],
    "elapsed": {
        "best": [],
        "worst": [],
    }
}
for i in range(1000, 100001, 1000):
    data = sample(range(100000), i)
    data.sort()
    dataToPlot['index'].append(i)

    # for best case
    middle = data[(i-1)//2]
    start = time()
    binary_search(data, 0, i-1, middle)
    elapsed = time() - start
    dataToPlot['elapsed']["best"].append(elapsed)

    # for worst case
    start = time()
    index = binary_search(data, 0, i-1, -1)
    elapsed = time() - start
    dataToPlot['elapsed']["worst"].append(elapsed)

plt.plot(dataToPlot["index"], dataToPlot["elapsed"]
         ["best"], c="green", label="Best Case")
plt.plot(dataToPlot["index"], dataToPlot["elapsed"]
         ["worst"], c="red", label="Worst Case")
plt.legend()
plt.show()
