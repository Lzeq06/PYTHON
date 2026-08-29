import sys
import math

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    i, s = map(int, entrada[:2])
    mmc = i
    for n in range(i + 1, s + 1):
        mmc = (mmc * n) // math.gcd(mmc, n)
    print(mmc)

if __name__ == "__main__":
    main()
