import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    m = int(entrada[1])
    entrosamento = [[0] * (n + 1) for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        x, y, z = map(int, entrada[idx:idx+3])
        idx += 3
        entrosamento[x][y] = z
        entrosamento[y][x] = z
    
    maior_soma = -1
    m1, m2, m3 = 1, 2, 3
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                soma = entrosamento[i][j] + entrosamento[i][k] + entrosamento[j][k]
                if soma > maior_soma:
                    maior_soma = soma
                    m1, m2, m3 = i, j, k
    print(f"{m1} {m2} {m3}")

if __name__ == "__main__":
    main()
