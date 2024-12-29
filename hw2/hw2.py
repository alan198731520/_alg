def perm(n):
    visited = [False] * n
    def dfs(path):
        if len(path) == n:
            print(path)
            return

        for x in range(n):
            if not visited[x]:
                visited[x] = True
                dfs(path + [x])
                visited[x] = False

    dfs([])

if __name__ == "__main__":
    for num in range(2, 6):
        print(f"Permutations of {num}:")
        perm(num)
        print()