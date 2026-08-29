import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    soma = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            soma += d
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        soma += n
    print(soma)

if __name__ == "__main__":
    main()
