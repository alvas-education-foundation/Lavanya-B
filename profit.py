# github repository- Lavanya-B

def solve(n, offers):
    dp=[0]*(n+1)
    for i in range(1, n+1):
        for sell, price in enumerate(offers, start=1):
            if sell>i:
                break
            dp[i]=max(dp[i], dp[i-sell]+price)
    return dp[n]

testCases=[
    [1, 5, 8, 9, 10, 17, 17, 20],
]
for offers in testCases:
    for sell, price in enumerate(offers, start=1):
        print(sell, [" pieces", " piece"][sell==1], ": ", price, "/-", sep="")
    print("Maximum profit:", solve(len(offers), offers))
    print()