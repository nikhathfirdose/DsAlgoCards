# Day 6 - Plus one
class Solution:
    def plusOne(self, digits):
        listToStr = ''.join([str(elem) for elem in digits]) 
        value = int(listToStr)+1
        return list(str(value))
            
# Day 7 - Island Perimeter
class Solutions:
    def islandPerimeter(self, grid) :
        if(len(grid)==0 or len(grid[0])==0): return 0
        perimeter=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print(grid[i][j])
                if(grid[i][j]==1):
                    perimeter+=4
                    if(i>0 and grid[i-1][j]==1):
                        perimeter-=2
                    if(j>0 and grid[i][j-1]==1):
                        perimeter-=2
                            # print(perimeter)
        return perimeter
                        