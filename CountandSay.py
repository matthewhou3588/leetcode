class Solution(object):      
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
        
            ret = ''
            pre = self.countAndSay(n-1)

            i = 0
            while i < len(pre):
                s = i
                while i < len(pre)-1 and pre[i] == pre[i+1]:
                    i += 1

                ret += str(i-s+1) + pre[s]
                
                i += 1

            return ret       
        
