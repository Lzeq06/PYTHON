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
    for a in range(2, n // 2 + 1):
        if eh_primo(a) and eh_primo(n - a):
            print("sim")
            return
    print("nao")

if __name__ == "__main__":
    main()
