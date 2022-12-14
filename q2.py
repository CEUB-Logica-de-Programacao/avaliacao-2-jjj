# Você está subindo uma escada. São necessários `n` degraus para chegar ao topo.
#
# Você pode subir 1 ou 2 degraus de cada vez. De quantas formas distintas você pode escalar até o topo?
#
# ### Exemplo 1
#
# ```
# Input: n = 2
# Output: 2
# Explicação: Existem duas maneiras de chegar ao topo.
# 1. 1 degrau + 1 degrau
# 2. 2 degraus
# ```
#
# ### Exemplo 2
#
# ```
# Input: n = 3
# Output: 3
# Explanation: Existem três maneiras de chegar ao topo.
# 1. 1 degrau + 1 degrau + 1 degrau
# 2. 1 degrau + 2 degraus
# 3. 2 degraus + 1 degrau
# ```


def q2(n):
    def fib(n, dp):
        if (n <= 1):
            return 1
        if(dp[n] != -1 ):
            return dp[n]
        dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
        return dp[n]
    def countWays(n):
        dp = [-1 for i in range(n + 1)]
        fib(n, dp)
        return dp[n]
    n = 3
    print("maneiras = " + str(countWays(n)))


if __name__ == '__main__':
    print(q2(2))
