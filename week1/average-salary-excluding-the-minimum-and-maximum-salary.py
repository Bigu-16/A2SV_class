class Solution:
    def average(self, salary: List[int]) -> float:
        # salary.sort()
        # num_before_last = len(salary) - 1
        # total = sum(salary[1:num_before_last])
        # average = total/(num_before_last-1)
        # return average
        return (sum(salary) -(max(salary)+min(salary)))/(len(salary)-2)