# Day 5 - Hamming distance
class Solution:
    def hammingDistance(self, x,y) :
        if(x>255  or y>255): 
            a = format(x,'032b') 
            b = format(y,'032b')
        else:
            a, b = format(x,'08b'), format(y,'08b')
        count=0
        i=0
        while i<len(a):
            if(a[i]!= b[i]):
                count+=1
            i+=1
        return count
        