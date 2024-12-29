def power2n_a(n):
    return 2**n

def power2n_b(n):
    if n == 0: return 1
    return power2n_b(n-1) + power2n_b(n-1)

def power2n_c(n):
    if n == 0: return 1
    return 2 * power2n_c(n-1)

def power2n_d(n, memo={}):
    if n in memo:  
        return memo[n]
    if n == 0: 
        return 1
    memo[n] = 2 * power2n_d(n-1, memo)
    return memo[n]

print('power2n_d(10) =', power2n_d(10))
print('power2n_d(40) =', power2n_d(40))