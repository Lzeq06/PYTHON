import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    t = int(entrada[0])
    for a in range(1, t // 3 + 1):
        for b in range(a + 1, t):
            c = t - a - b
            if c > b and a * a + b * b == c * c:
                print(f"{a} {b} {c} {a * b * c}")

if __name__ == "__main__":
    main()
