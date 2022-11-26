import random
import string


def generate_random_string(n: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


def generate_random_string_contains_expected(expected: str, n: int) -> str:
    if len(expected) > n:
        raise ValueError(
            f"Expected character length({len(expected)}) must be greater than n({n})."
        )

    insert_position = random.randint(0, n)
    random_string = generate_random_string(n - len(expected))
    return random_string[:insert_position] + expected \
        + random_string[insert_position:]
