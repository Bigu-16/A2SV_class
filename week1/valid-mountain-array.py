class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag = True

        if len(arr) < 3:
            return False
        if arr[0] > arr[1]:
            return False

        for i in range(len(arr)-1):

            if arr[i] == arr [i+1]:
                return False

            if flag:
                if arr[i] < arr[i+1]:
                    continue
                else:
                    flag = False

            else:
                if arr[i] < arr[i+1]:
                    return False
        if flag:
            return False
        return True
       