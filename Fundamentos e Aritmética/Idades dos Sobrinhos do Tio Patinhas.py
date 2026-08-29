import sys

def main():
    entrada = sys.stdin.read().split()
    for i in range(0, len(entrada), 3):
        bloco = entrada[i:i+3]
        if len(bloco) < 3:
            break
        h, z, l = map(int, bloco)
        if h < z and h < l:
            print("huguinho")
        elif z < h and z < l:
            print("zezinho")
        else:
            print("luisinho")

if __name__ == "__main__":
    main()
