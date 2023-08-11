T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    prices = list(map(int, input().strip().split()))
    
    maxProfit = 0
    maxPrice = prices[-1]
    
    for j in range(N-2, -1, -1):
        if prices[j] < maxPrice:
            maxProfit += maxPrice - prices[j]
        else:
            maxPrice = prices[j]
    
    print(maxProfit)
