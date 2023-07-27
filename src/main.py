from utils.args import getArgs
from utils.clock import clock
from utils.lerps import lin_lerp, sig_lerp
from utils.dice import dice


def main():
    args = getArgs()

    dt = args.dt
    lerp = lin_lerp if args.lin else sig_lerp
    c1 = args.c1
    c2 = args.c2
    t = args.t
    r = args.r
    random = args.random

    for _ in range(r):
        if not random:
            clock(t, dt, lerp, c1, c2)
            c1, c2 = c2, c1
        else:
            c2 = [dice(0, 255), dice(0, 255), dice(0, 255)]
            clock(t, dt, lerp, c1, c2)
            c1 = c2


if __name__ == "__main__":
    main()
