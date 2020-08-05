def solution(triangle):
    dp = triangle
    n = len(triangle)

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] += triangle[i-1][j]
            elif j == i:
                dp[i][j] += triangle[i-1][j-1]
            else:
                dp[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    answer = max(dp[n-1])
    return answer