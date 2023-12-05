class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # find the shortest word length
        shortestword = float('inf')
        for word in strs:
            shortestword = min(shortestword,len(word))

        #for i in range(len(shortestword))
        prefix = ""
        for i in range(shortestword):
            currentchar = strs[0][i]
            #for word in strs - i , i+1
            for words in strs:

                # fail
                if words[i] != currentchar:
                    return prefix
                
                    #return
            
            #update our result
            prefix += currentchar

        #return result
        return prefix