def seconds_to_hms(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def celsius_to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 1)


def split_evenly(total, people):
    return total // people, total % people


def initials(full_name):
    parts = full_name.split()
    result = ""
    i = 0
    while i < len(parts):
        result += parts[i][0].upper()
        i += 1
    return result


def is_palindrome_word(word):
    w = word.strip().lower()
    return w == w[::-1]


def mask_email(email):
    at = email.index("@")
    local = email[:at]
    return local[0] + "*" * (len(local) - 1) + email[at:]


def middle(values):
    n = len(values)
    if n == 0:
        return []
    if n % 2 == 1:
        return values[n // 2]
    return values[n // 2 - 1 : n // 2 + 1]


def rotate_left(values, k):
    n = len(values)
    if n == 0:
        return []
    k = k % n
    return values[k:] + values[:k]


def fib_list(n):
    result = []
    a, b = 0, 1
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
