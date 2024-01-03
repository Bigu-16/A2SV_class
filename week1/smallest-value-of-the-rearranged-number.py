class Solution:
    def smallestNumber(self, num: int) -> int:
        
        num_list = list(str(num))
        ans = ''

        if num < 0:
            sorted_num = num_list[1:]
            sorted_num.sort(reverse = True)
            ans = "".join(sorted_num)
            ans = int(ans) * -1
        elif num>0:
            num_list.sort()
            c = num_list.count('0')
            num_list[0],num_list[c] = num_list[c],num_list[0]
            ans = ''.join(num_list)
            ans = int(ans)
        else:
            return 0
        return ans

           