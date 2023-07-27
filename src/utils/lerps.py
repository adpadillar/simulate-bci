def lin_lerp(a, b, t):
    return a + (b - a) * t


def sig_lerp(a, b, t):
    return a + (b - a) * (t ** 2 * (3 - 2 * t))
