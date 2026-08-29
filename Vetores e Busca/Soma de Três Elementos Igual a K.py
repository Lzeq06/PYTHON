import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    n = int(entrada[0])
    v = [int(x) for x in entrada[1:n+1]]
    k = int(entrada[n+1])
    
    for i in range(n):
        for j in range(i + 1, n):
            for l in range(j + 1, n):
                if v[i] + v[j] + v[l] == k:
                    print("SIM")
                    return
    print("NAO")

if __name__ == "__main__":
    main()
