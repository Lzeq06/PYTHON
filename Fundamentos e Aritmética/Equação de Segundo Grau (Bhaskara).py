import sys
import math

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    a, b, c = map(float, entrada[:3])
    
    if a != 0:
        d = b * b - 4 * a * c
        if d >= 0:
            r1 = (-b - math.sqrt(d)) / (2 * a)
            r2 = (-b + math.sqrt(d)) / (2 * a)
            print(f"{r1} {r2}")
            return
    print("Como b^2 - 4ac < 0, as raizes serao numeros complexos")

if __name__ == "__main__":
    main()
