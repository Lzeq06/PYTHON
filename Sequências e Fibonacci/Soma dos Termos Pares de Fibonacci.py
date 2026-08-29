import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    k = int(entrada[0])
    a, b, soma = 0, 1, 0
    while a <= k:
        if a % 2 == 0:
            soma += a
        a, b = b, a + b
    print(soma)

if __name__ == "__main__":
    main()
