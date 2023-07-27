import argparse


def getArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument("--dt", type=float, default=1e-2)
    parser.add_argument("--lin", type=bool, default=True)
    parser.add_argument("--sig", type=bool, default=False)
    parser.add_argument("--t", type=int, default=10)
    parser.add_argument("--c1", type=int, nargs=3, default=[0, 0, 0])
    parser.add_argument("--c2", type=int, nargs=3, default=[255, 255, 255])
    parser.add_argument("--r", type=int, default=2)
    parser.add_argument("--mode", type=str, default="rgb")
    parser.add_argument("--random", type=bool, default=False)

    return parser.parse_args()
