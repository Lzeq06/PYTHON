import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    maior = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            maior = d
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        maior = n
    print(maior)

if __name__ == "__main__":
    main()
