class KnapsackPack:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight

    def __lt__(self, other):
        return self.cost < other.cost

def knapsackGreedyFrac(cap, wt, val, n):
    packs = []
    for i in range(n):
        packs.append(KnapsackPack(wt[i], val[i]))

    packs.sort(reverse = True)

    totVal = 0
    for i in packs:
        curWt = i.weight
        curVal = i.value

        if cap - curWt >= 0:
            cap -= curWt
            totVal += curVal
        else:
            fraction = cap / curWt
            totVal += curVal * fraction
            cap = int(cap - (curWt * fraction))
            break

    return int(totVal)
