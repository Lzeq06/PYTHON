import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    lados = sorted(map(int, entrada[:3]))
    a, b, c = lados[0], lados[1], lados[2]
    if a + b <= c:
        print("n")
    elif a * a + b * b == c * c:
        print("r")
    elif a * a + b * b > c * c:
        print("a")
    else:
        print("o")

if __name__ == "__main__":
    main()
