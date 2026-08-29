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
    soma = sum(n for n in range(i, s + 1) if n % 10 == 3 and eh_primo(n))
    print(soma)

if __name__ == "__main__":
    main()
