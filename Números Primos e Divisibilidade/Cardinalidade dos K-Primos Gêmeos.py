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
    i, k, s = map(int, entrada[:3])
    c = 0
    for x in range(i, s - k + 1):
        if eh_primo(x) and eh_primo(x + k):
            c += 1
    print(c)

if __name__ == "__main__":
    main()
