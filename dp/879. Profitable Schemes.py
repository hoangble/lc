def profitableSchemes(G, P, group, profit):
    dp = [[0] * (G + 1) for i in range(P + 1)]
    dp[0][0] = 1
    for p, g in zip(profit, group):
        for i in range(P, -1, -1):
            for j in range(G - g, -1, -1):
                dp[min(i + p, P)][j + g] += dp[i][j]
    return sum(dp[P]) % (10**9 + 7)


n = 5
minProfit = 3
group = [2, 2]
profit = [2, 3]

profitableSchemes(n, minProfit, group, profit)
