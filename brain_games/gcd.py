def gcd(a: int, b: int) -> int:
    first_number = a if a > b else b
    second_number = a if b > a else b
    remainder = 0
    while True:
        remainder = first_number % second_number
        if not remainder:
            break
        first_number = second_number
        second_number = remainder
    return second_number
