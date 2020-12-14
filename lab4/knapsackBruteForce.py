def knapSackBrut01(wt, val, cap, n):

    if n == 0 or cap == 0 :
        return 0

    if (wt[n-1] > cap):
        return knapSackBrut01(wt, val, cap, n-1)

    else:
        return max(val[n-1] + knapSackBrut01(wt, val, cap-wt[n-1], n-1),
                   knapSackBrut01(wt, val, cap, n-1))

def knapSackBrutFrac(wt, val, cap, n):

    maxProfit = 0
    solutions = [format(x, '03b') for x in range(2**n)]

    for sol in solutions:

        i_element = []

        for i, x in enumerate(sol):
            if x == '0':
                i_element.append(i)

        profit = sum(int(sol[i])*val[i] for i in range(n))
        weight = sum(int(sol[i])*wt[i] for i in range(n))

        fraction = 0

        if weight < cap:

            for i in i_element:
                if cap-weight < wt[i]:
                    remain = cap - weight

                else:
                    remain = wt[i]

                frac = (val[i] / wt[i]) * remain
                if frac > fraction:
                    fraction = frac

        profit += fraction

        if weight <= cap and profit >= maxProfit:
            maxProfit = profit

    return int(maxProfit)
