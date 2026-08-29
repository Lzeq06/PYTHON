import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    taxas = [int(x) for x in entrada[1:n+1]]
    max_lucro = -40000000
    for i in range(n - 3):
        temp = sum(taxas[i:i+4])
        if temp > max_lucro:
            max_lucro = temp
    print(max_lucro)

if __name__ == "__main__":
    main()
