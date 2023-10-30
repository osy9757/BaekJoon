def lcs(S1, S2):
    m, n = len(S1), len(S2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]

    lcs_string = ""
    while m > 0 and n > 0:
        if S1[m - 1] == S2[n - 1]:
            lcs_string = S1[m - 1] + lcs_string
            m -= 1
            n -= 1
        elif dp[m - 1][n] > dp[m][n - 1]:
            m -= 1
        else:
            n -= 1

    return lcs_length, lcs_string

S1 = input()
S2 = input()

lcs_length, lcs_string = lcs(S1, S2)
print(lcs_length)
print(lcs_string)