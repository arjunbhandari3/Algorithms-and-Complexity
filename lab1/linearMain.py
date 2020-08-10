import random
from search import linear_search
from time import time
import matplotlib.pyplot as plt
dataToPlot = {
    "index": [],
    "elapsed": {
        "best": [],
        "worst": [],
    }
}

for i in range(1000, 100001, 1000):
    data = random.sample(range(100000), i)
    dataToPlot['index'].append(i)

    # for best case
    start = time()
    linear_search(data, data[0])
    elapsed = time() - start
    dataToPlot['elapsed']["best"].append(elapsed)

    # for worst case
    start = time()
    linear_search(data, -10000)
    elapsed = time() - start
    dataToPlot['elapsed']["worst"].append(elapsed)

plt.plot(dataToPlot["index"], dataToPlot["elapsed"]
         ["best"], c="green", label="Best Case")
plt.plot(dataToPlot["index"], dataToPlot["elapsed"]
         ["worst"], c="red", label="Worst Case")
plt.legend()
plt.show()
