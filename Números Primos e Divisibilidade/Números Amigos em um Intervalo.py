import sys

def soma_divisores(n):
    if n <= 1:
        return 0
    soma = 1
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            soma += d
            if d * d != n:
                soma += n // d
    return soma

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    i, s = map(int, entrada[:2])
    for a in range(i, s + 1):
        b = soma_divisores(a)
        if a < b <= s and soma_divisores(b) == a:
            print(f"{a} {b}")

if __name__ == "__main__":
    main()
