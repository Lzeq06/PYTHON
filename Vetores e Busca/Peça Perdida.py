import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    pecas = [int(x) for x in entrada[1:n]]
    soma_esperada = n * (n + 1) // 2
    print(soma_esperada - sum(pecas))

if __name__ == "__main__":
    main()
