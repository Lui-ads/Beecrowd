# Fatores e Múltiplos
# Fiz com ajuda
import sys
from typing import List

def main():
    input = sys.stdin.read().split()
    ptr = 0
    casos = int(input[ptr])
    ptr += 1
    MAXN = 1000  # Adjust based on problem constraints
    for caso in range(1, casos + 1):
        grafo = [[] for _ in range(MAXN)]
        vetor = [0] * (2 * MAXN)
        
        n = int(input[ptr])
        ptr += 1
        for i in range(1, n + 1):
            vetor[i] = int(input[ptr])
            ptr += 1
        
        m = int(input[ptr])
        ptr += 1
        for i in range(n + 1, n + m + 1):
            vetor[i] = int(input[ptr])
            ptr += 1
        
        # Build bipartite graph
        for i in range(1, n + 1):
            for j in range(n + 1, n + m + 1):
                if vetor[i] == vetor[j] or (vetor[i] != 0 and vetor[j] % vetor[i] == 0):
                    grafo[i].append(j)
        
        match = [-1] * (n + m + 2)  # Right side nodes
        
        def dfs(u, visited):
            for v in grafo[u]:
                if not visited[v]:
                    visited[v] = True
                    if match[v] == -1 or dfs(match[v], visited):
                        match[v] = u
                        return True
            return False
        
        resposta = 0
        for i in range(1, n + 1):
            visited = [False] * (n + m + 2)
            if dfs(i, visited):
                resposta += 1
        
        print(f"Case {caso}: {resposta}")

if __name__ == "__main__":
    main()