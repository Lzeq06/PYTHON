import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    quantidades = [int(x) for x in entrada[1:n+1]]
    print(min(quantidades))

if __name__ == "__main__":
    main()
