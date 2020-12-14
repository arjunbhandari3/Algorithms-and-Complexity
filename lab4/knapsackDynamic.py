def knapSackDynamic (W, wt, val, n):
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):

            if i == 0 or j == 0:
                table[i][j] = 0

            elif wt[i-1] <= j:
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]],  table[i-1][j])

            else:
                table[i][j] = table[i-1][j]

    return table[n][W]
