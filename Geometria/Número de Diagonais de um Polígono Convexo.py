import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    print(n * (n - 3) // 2)

if __name__ == "__main__":
    main()
