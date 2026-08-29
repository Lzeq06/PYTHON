import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    if n == 0:
        print(0)
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, (a + b) % 10
        print(b)

if __name__ == "__main__":
    main()
