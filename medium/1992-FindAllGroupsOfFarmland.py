from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        farmlands = []

        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0:
                    continue

                min_x, min_y, max_x, max_y = i, j, i, j

                while max_x < len(land):
                    if land[max_x][j] == 0:
                        break
                    max_x += 1
                max_x -= 1

                while max_y < len(land[0]):
                    if land[i][max_y] == 0:
                        break
                    max_y += 1
                max_y -= 1

                farmlands.append([min_x, min_y, max_x, max_y])

                for x in range(min_x, max_x + 1):
                    for y in range(min_y, max_y + 1):
                        land[x][y] = 0

        return farmlands
