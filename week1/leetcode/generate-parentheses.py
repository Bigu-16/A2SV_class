class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bucket = []
        ans = set()
        pos = ("(" * n) +( ')' *n)

        count = 0

        def backtrack(i,count):
            # print(i, count) 
            if len(bucket) == 2*n and count == 0:
                ans.add(''.join(bucket[:]))
                return 
            if count > n or count < 0 or len(bucket) >= 2*n:
                return

            val = None
            for i in range(len(pos)):
            
                if pos[i] != val:
                    if pos[i] == "(":
                        bucket.append(pos[i])
                        backtrack(i+1,count + 1)
                        val = bucket.pop()
                    else:
                        bucket.append(pos[i])
                        backtrack(i+1,count -1)
                        val = bucket.pop()
            
        backtrack(0,0)
        return list(ans)