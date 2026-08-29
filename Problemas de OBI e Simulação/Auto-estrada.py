import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    c = int(entrada[0])
    s = entrada[1] if len(entrada) > 1 else ""
    valores = {'P': 2, 'C': 2, 'A': 1, 'D': 0}
    paineis = sum(valores.get(ch, 0) for ch in s[:c])
    print(paineis)

if __name__ == "__main__":
    main()
