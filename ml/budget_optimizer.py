def optimize(assets, budget):
    # assets = [(asset_id, cost, failure_prob, loss)]
    n=len(assets)
    dp=[[0]*(budget+1) for _ in range(n+1)]

    for i in range(1,n+1):
        aid,c,p,l=assets[i-1]
        val=p*l-c
        for b in range(budget+1):
            if c<=b:
                dp[i][b]=max(dp[i-1][b], dp[i-1][b-c]+val)
            else:
                dp[i][b]=dp[i-1][b]
    return dp[n][budget]
