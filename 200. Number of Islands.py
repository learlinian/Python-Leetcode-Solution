class Solution(object):
    def numIslands(self, grid):
        visited_island_pixel = {}   # record all visited pixels which are island ("1")
        count = 0                   # count the number of islands

        # function to find all island pixel ("1") around current pixel
        def check_1(i, j):
            adjacent = []
            for choice in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:     # 4 directions around the current pixel
                row = choice[0]
                col = choice[1]
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':  # record island pixel in dict
                    if row not in visited_island_pixel.keys():
                        visited_island_pixel[row] = [col]
                        adjacent.append([row, col])
                    elif col not in visited_island_pixel[row]:
                        visited_island_pixel[row].append(col)
                        adjacent.append([row, col])
            return adjacent

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i not in visited_island_pixel.keys() or j not in visited_island_pixel[i]:
                    if grid[i][j] == '1':
                        adjacent_pixels = check_1(i, j)
                        while adjacent_pixels:
                            print(visited_island_pixel, adjacent_pixels)
                            adjacent_pixels = adjacent_pixels + check_1(adjacent_pixels[0][0], adjacent_pixels[0][1])
                            del adjacent_pixels[0]
                        count += 1
        print(visited_island_pixel)
        return count


if __name__ == '__main__':
    # grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    # grid = [['1', '1', '1'], ['0', '1', '0'], ['1', '1', '1']]
    grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
    print(Solution().numIslands(grid))
