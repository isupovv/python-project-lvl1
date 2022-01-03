from typing import Text


def is_prime(n: int) -> Text:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    if d * d > n:
        return 'yes'
    return 'no'
