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
    if len(entrada) == 1:
        i, s = 1, int(entrada[0])
    else:
        i, s = int(entrada[0]), int(entrada[1])
    c = sum(1 for n in range(i, s + 1) if eh_primo(n))
    print(c)

if __name__ == "__main__":
    main()
