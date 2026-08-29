import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    a, b = map(float, entrada[:2])
    if a != 0:
        print(-b / a)
    else:
        print("A equacao nao possui raiz unica")

if __name__ == "__main__":
    main()
