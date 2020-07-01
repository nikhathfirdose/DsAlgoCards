# Arrange coins
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        index=1
        while(n>=index):
            count+=1
            n=n-index
            index=index+1
        return count
class Solutions():
    def arrangeCoins(self, n):
        if(n==0):
            return 0
        current=1
        rem = n-1
        while(rem>=current+1):
            current+=1
            rem-=current
          
        return current