import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    c, p, f = map(int, entrada[:3])
    print("S" if c * f <= p else "N")

if __name__ == "__main__":
    main()
