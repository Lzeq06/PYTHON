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
    i, s = map(int, entrada[:2])
    primos = [str(n) for n in range(i, s + 1) if eh_primo(n)]
    if primos:
        print(" ".join(primos))

if __name__ == "__main__":
    main()
