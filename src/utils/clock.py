import time


def clock(t, dt, lerp, c1, c2):
    iterations = t / dt
    for i in range(1, int(iterations) + 1):
        r1, g1, b1 = c1
        r2, g2, b2 = c2
        r = int(lerp(r1, r2, i / iterations))
        g = int(lerp(g1, g2, i / iterations))
        b = int(lerp(b1, b2, i / iterations))
        print(f"{r},{g},{b}")
        time.sleep(dt - dt / 5.5)
