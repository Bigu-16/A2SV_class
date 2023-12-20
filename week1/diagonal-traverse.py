class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mat_dict = defaultdict(list)

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                sums = row + col
                mat_dict[sums].append(mat[row][col])
        
        ans = []
        for sums,value in mat_dict.items():
            if sums % 2 == 0:
                value.reverse()
                ans.extend(value)
            else:
                ans.extend(value)
        return ans
