from pprint import pp
from scipy.stats import binom


def percent(value, decimals=2):
    return f"{value:.{decimals}%}"


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


def main():
    k = 6  # successes
    n = 12  # trials
    p = 0.5  # probability of success
    inputs = [[k, n, p], [2, n, 0.75]]
    binom.
    [pp(percent(binom.cdf(k, n, p), 4)) for k, n, p in inputs]


if __name__ == "__main__":
    main()
