import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    soma = n * (n + 1) // 2
    soma_quadrados = n * (n + 1) * (2 * n + 1) // 6
    diferenca = (soma ** 2) - soma_quadrados
    print(diferenca)

if __name__ == "__main__":
    main()
