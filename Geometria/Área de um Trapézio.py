import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    b1, b2, h = map(float, entrada[:3])
    print((b1 + b2) * h / 2)

if __name__ == "__main__":
    main()
