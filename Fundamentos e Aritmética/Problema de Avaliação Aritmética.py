import sys

def main():
    entrada = sys.stdin.read().split()
    if len(entrada) >= 4:
        n = int(entrada[0])
        p = int(entrada[1])
        c = entrada[2]
        q = int(entrada[3])
        resultado = p + q if c == '+' else p * q
        print("OK" if resultado <= n else "OVERFLOW")

if __name__ == "__main__":
    main()
