class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        rtv = -1
        
        if needle == None:
            return -1
        if len(needle) == 0:
            return 0
        
        
        for i in range(len(haystack)-len(needle)+1):
            flag = 0
            for j in range(len(needle)):
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                    flag = 1
                    break
            if flag == 0:
                rtv = i - len(needle)
                break
                
        return rtv
                    
            
                
            
                    
            
