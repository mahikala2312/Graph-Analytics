def maxRegion(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    visited = [[False] * cols for _ in range(rows)]
    
    # 8 possible directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        
        if grid[r][c] == 0 or visited[r][c]:
            return 0
        
        visited[r][c] = True
        count = 1
        
        for dr, dc in directions:
            count += dfs(r + dr, c + dc)
        
        return count
    
    largest = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                size = dfs(i, j)
                largest = max(largest, size)
    
    return largest


# Input
rows = int(input())
cols = int(input())

grid = []

for i in range(rows):
    grid.append(list(map(int, input().split())))

print(maxRegion(grid))