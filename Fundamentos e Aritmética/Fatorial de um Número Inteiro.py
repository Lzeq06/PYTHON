import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    f = 1
    for i in range(2, n + 1):
        f *= i
    print(f)

if __name__ == "__main__":
    main()
