class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        sum1 = 0

        
        j = 0
        while j < len(processorTime):
            for i in range(0,len(tasks),4):
                sum1 = max(sum1, tasks[i]+processorTime[j])
                j += 1

        return sum1
        