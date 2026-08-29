import sys
import math

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    x1, y1, x2, y2 = map(float, entrada[:4])
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(dist)

if __name__ == "__main__":
    main()
