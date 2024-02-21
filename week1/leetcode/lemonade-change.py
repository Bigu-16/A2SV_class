class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_dict = defaultdict(int)

        for i in range(len(bills)):
            bill_dict[bills[i]] += 1
            if bills[i] == 10:
                if bill_dict[5]:
                    bill_dict[5] -= 1
                else:
                    return False
            elif bills[i] == 20:
                if bill_dict[5] and bill_dict[10]:
                    bill_dict[5] -= 1
                    bill_dict[10] -= 1
                    bill_dict[20] -= 1
                elif bill_dict[5] > 2:
                    bill_dict[5] -= 3
                    bill_dict[20] -= 1 
                else:
                    return False
        return True