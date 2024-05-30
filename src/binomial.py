def binomial_coeff(k: int, n: int):
    """Calculate the binomial coefficient"""
    if k == 0:
        return 1
    if 2 * k > n:
        k = n - k
    result = n
    for i in range(2, k + 1):
        result *= n - i + 1
        result //= i
    return result


def binomial_pmf(k: int, n: int, p: float):
    """Probability mass function"""
    return binomial_coeff(n, k) * p**k * (1 - p) ** (n - k)


def binomial_cdf(k: int, n: int, p: float):
    """Cumulative distribution function"""
    return sum(binomial_pmf(n, p, i) for i in range(k + 1))
