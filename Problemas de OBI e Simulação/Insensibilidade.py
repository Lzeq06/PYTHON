import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    total = 0
    idx = 1
    for _ in range(n):
        x1, y1, x2, y2 = map(int, entrada[idx:idx+4])
        idx += 4
        total += (x1 - x2) ** 2 + (y1 - y2) ** 2
    print(total)

if __name__ == "__main__":
    main()
