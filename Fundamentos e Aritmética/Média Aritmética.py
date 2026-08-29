import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n1, n2 = map(float, entrada[:2])
    print((n1 + n2) / 2)

if __name__ == "__main__":
    main()
