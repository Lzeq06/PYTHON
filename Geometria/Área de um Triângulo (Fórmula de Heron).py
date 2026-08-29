import sys
import math

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    a, b, c = map(float, entrada[:3])
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(area)

if __name__ == "__main__":
    main()
