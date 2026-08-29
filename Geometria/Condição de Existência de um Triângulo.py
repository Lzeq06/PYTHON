import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    a, b, c = map(float, entrada[:3])
    if a + b > c and a + c > b and b + c > a:
        print("Forma um triangulo")
    else:
        print("Nao forma um triangulo")

if __name__ == "__main__":
    main()
