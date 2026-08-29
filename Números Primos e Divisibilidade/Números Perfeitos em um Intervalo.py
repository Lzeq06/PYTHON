import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    i, s = map(int, entrada[:2])
    res = []
    for n in range(i, s + 1):
        if n > 1:
            soma = 1
            for d in range(2, int(n ** 0.5) + 1):
                if n % d == 0:
                    soma += d
                    if d * d != n:
                        soma += n // d
            if soma == n:
                res.append(str(n))
    if res:
        print(" ".join(res))

if __name__ == "__main__":
    main()
