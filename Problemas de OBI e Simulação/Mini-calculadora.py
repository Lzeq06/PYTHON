import sys
import math

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n, d, q = map(int, entrada[:3])
    divisor = math.gcd(d, q)
    r = d // divisor
    p = q // divisor
    if n < 60 and (r >= (1 << n) or p >= (1 << n)):
        print("IMPOSSIVEL")
    else:
        print(f"{r} {p}")

if __name__ == "__main__":
    main()
