import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    c = 0
    for i in range(1, n):
        if n % i == 0:
            c += 1
    print(c)

if __name__ == "__main__":
    main()
