import sys

def eh_primo(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    f = n * n + n + 41
    print(f"{f} {'sim' if eh_primo(f) else 'não'}")

if __name__ == "__main__":
    main()
