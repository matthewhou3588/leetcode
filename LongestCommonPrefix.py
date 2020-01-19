class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        return_v = ''        
        
        if len(strs) == 0:
            return return_v
        if len(strs) == 1:
            return strs[0]
        
        min_len = min([len(s)  for s in strs ])
        
        if min_len == 0:
            return return_v
                
        for i in range(min_len):
            tmp = strs[0][i]
            return_v += tmp
            
            for st in strs:
                if st[i] != tmp:
                    return return_v[:-1]
                else:
                    continue
                    
        return return_v
