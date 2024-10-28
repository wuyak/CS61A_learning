from ucb import trace


@trace
def count_partitions(n, m):
    """
    dp[n][m] = dp[n-m][m]+dp[n][m-1]
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return with_m + without_m
