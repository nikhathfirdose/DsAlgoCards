# Day3 - Prison with n cells
class Solution:
    def prisonAfterNDays(self, cells, N):
        _map = {}
        self.cells = cells
        for i in range(N):
            s = str(self.cells)
            if s in _map:
                loop_len = i- _map[s]
                rem_days = (N-i)% loop_len
                return self.prisonAfterNDays(self.cells, rem_days)
            else:
                _map[s] =i
                prev = self.cells[0]
                for j in range(1,7):
                    curr, next = self.cells[j], self.cells[j+1]
                    self.cells[j] = 1- (prev^next)
                    prev = curr
            self.cells[0], self.cells[7]=0,0
            
        return self.cells
        